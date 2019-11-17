## EXERCICE: Importer un CSV dans une base de données

### Correction

```python
# -*- coding: utf-8 -*-
import csv
import sqlite3

db = sqlite3.connect('../chinook/chinook.db')
print 'Database connectée'

with open('music.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for i, row in enumerate(csv_reader):
        if i != 0:
            artist_name = row[2]

            # see https://stackoverflow.com/questions/36765835/inserting-text-having-single-quote-in-sqlite-database
            requete = ''' INSERT INTO artists (name) VALUES (?); '''

            # insert artist name into artists tables
            db.execute(requete, (artist_name,))

    db.commit()

db.close()
print 'Database fermée'
```
