## EXERCICE: Exporter les morceaux durant moins d'une minute vers un fichier CSV

### Solution

```python
# -*- coding: utf-8 -*-

import csv
import sqlite3


# 1. read data from database
db = sqlite3.connect('../chinook/chinook.db')
print 'Database connectée'

# read from db
requete = "SELECT * FROM tracks WHERE Milliseconds < 60000"
results = db.execute(requete)

# convert to list
short_songs = list(results)

# check results
for song in short_songs:
    print song

db.close()
print 'Database fermée'


print "-"*10
print "%s chansons dans la base de données"%len(short_songs)

# 2. write CSV file
column_names = ["TrackId", "Name", "AlbumId", "Albu", "MediaTypeId", "GenreId", "Composer", "Milliseconds", "Bytes", "UnitPric"]

with open('short_songs.csv', "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    # write headers
    writer.writerow(column_names)

    # count rows
    count_rows = 0

    # write to CSV
    for song in short_songs:
        encoded = [unicode(s).encode("utf-8") for s in song] # decode characters
        writer.writerow(encoded)
        count_rows = count_rows + 1

print "-"*10
print "%s chansons dans le fichier CSV"%count_rows
```
