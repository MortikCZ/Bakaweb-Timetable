import requests
from bs4 import BeautifulSoup
import json
import re
from collections import defaultdict

def download_html(url):
    """Stáhne HTML obsah z dané URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch URL: {url}") from e

def extract_timetable_data(html_content):
    """Extrahuje data rozvrhu z HTML."""
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
        raise ValueError("Timetable table not found in the HTML content.")

def filter_data(data_details):
    """Filtruje a organizuje data rozvrhu."""
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
            filtered_data["unknown"].append(entry)
    return filtered_data

def save_data(filtered_data, output_file):
    """Uloží filtrovaná data do JSON souboru."""
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(filtered_data, file, ensure_ascii=False, indent=4)

def get_timetable(url, output_file):
    """Stáhne HTML obsah z dané URL, extrahuje data rozvrhu, filtrovaná data uloží do JSON souboru."""
    html_content = download_html(url)
    data_details = extract_timetable_data(html_content)
    filtered_data = filter_data(data_details)
    save_data(filtered_data, output_file)
