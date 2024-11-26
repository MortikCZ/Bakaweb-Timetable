import requests
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict

def download_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page from {url}. Status code: {response.status_code}")
        return None

def extract_timetable_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    timetable_table = soup.find("div", id="main", class_="bk-timetable-main")

    if timetable_table:
        data_details = []
        for item in timetable_table.find_all("div", class_="day-item-hover"):
            data_detail = item.get("data-detail")
            if data_detail:
                data_details.append(json.loads(data_detail))
        return data_details
    else:
        print("Timetable table not found in the HTML content.")
        return []

def filter_and_save_data(data_details, output_file):
    filtered_data = defaultdict(list)
    for entry in data_details:
        subjecttext = entry.get("subjecttext", "")
        match = re.match(r"(.+?) \| (.+?) \| (.+)", subjecttext)
        if match:
            subject, date, hour = match.groups()
            filtered_data[date].append({
                "subject": subject,
                "hour": hour,
                "room": entry.get("room", ""),
                "group": entry.get("group", ""),
                "changeinfo": entry.get("changeinfo", ""),
                "removedinfo": entry.get("removedinfo", ""),
                "type": entry.get("type", ""),
                "absentinfo": entry.get("absentinfo", ""),
                "InfoAbsentName": entry.get("InfoAbsentName", "")
            })
        else:
            match = re.match(r"(.+?) \| (.+)", subjecttext)
            if match:
                date, hour = match.groups()
                filtered_data[date].append({
                    "subject": "",
                    "hour": hour,
                    "room": entry.get("room", ""),
                    "group": entry.get("group", ""),
                    "changeinfo": entry.get("changeinfo", ""),
                    "removedinfo": entry.get("removedinfo", ""),
                    "type": entry.get("type", ""),
                    "absentinfo": entry.get("absentinfo", ""),
                    "InfoAbsentName": entry.get("InfoAbsentName", "")
                })
            else:
                filtered_data["unknown"].append(entry)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)
        print(f"Filtered data has been saved to {output_file}")

def get_timetable(url, output_file):
    html_content = download_html(url)
    if html_content:
        data_details = extract_timetable_data(html_content)
        filter_and_save_data(data_details, output_file)