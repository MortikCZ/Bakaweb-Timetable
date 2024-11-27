<div align="center">

  <h1>Bakaweb Timetable</h1>

  ![GitHub](https://img.shields.io/github/license/MortikCZ/Bakaweb-Timetable)
  ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MortikCZ/Bakaweb-Timetable)
  ![GitHub last commit](https://img.shields.io/github/last-commit/MortikCZ/Bakaweb-Timetable)

  <p>Jednoduchý nástroj pro extrakci rozvrhu z modulu Timetable Bakawebu. Data jsou získavána v HTML formátu a následně zpracována do JSON formátu.</p>
  
</div>

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




