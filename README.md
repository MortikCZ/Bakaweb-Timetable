# Bakaweb Timetable
Jednoduchý nástroj pro extrakci rozvrhu z modulu Timetable Bakawebu. Data jsou získavána v HTML formátu a následně zpracována do JSON formátu.

## Licence
Tento projekt je licencován pod licencí MIT. Pro více informací se podívejte do souboru `LICENSE`.

## Příklad použítí
```python
import bakaweb_timetable

url = "https://bakalari.skola.cz/bakaweb/Timetable/Public/Permanent/Class/4U"
output_file = "timetable.json"
bakaweb_timetable.get_timetable(url, output_file)
```

Je zapotřebí předat funkci `get_timetable` URL adresu rozvrhu a název souboru, do kterého se má rozvrh uložit, viz. příklad výše.




