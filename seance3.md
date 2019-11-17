# Importer / Exporter des données

## Révisions du vocabulaire

Qu'avons-nous utilisé ?

- programmes
- languages
- concepts / mots nouveaux

## Lire un fichier CSV

Vous trouverez tous ces exemples dans le dossier [`./music`](https://github.com/clemsos/db-debutants/tree/master/music)

### Le fichier de données

Nous allons utiliser le jeu de données [Million Song Dataset](http://millionsongdataset.com/).

Télécharger [un échantillon](./music/music.csv).  
Comment est-t-il structuré (headers, séparateurs, etc.) ?

### Ouvrir un fichier CSV avec Python

La librairie [`csv`](https://docs.python.org/fr/3/library/csv.html) de Python sert à lire des fichiers de données.

```python
import csv

# ouvrir le fichier
with open('music.csv') as csv_file:
    # lire les données au formart csv
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(row)
```

### Compter le nombre de lignes dans le fichier

```python
import csv

with open('music.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1

print "Il y a %s lignes dans ce fichier"%line_count
# Le fichier CSV nommé `music.csv` contient 10000 enregistrements.
```

## Importer un CSV dans une base de données

Nous allons maintenant importer le fichier `music.csv` dans la base de données `chinook.db` en utilisant un script Python.

### Les étapes

Voici les étapes :

1. télécharger le [jeu de données](./music/music.csv)
2. lire les partie intéressantes (chansons, auteurs, titres d'albums)
3. les inscrire dans notre base de données.

### Exercice : importer les artistes du CSV dans Chinook

Exemple

```python
import csv
import sqlite3

conn = sqlite3.connect('chinook.db')
print 'Database connectée'

with open('music.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        artist_name = row[2]

        # insert artist name into artists tables


db.close()
print 'Database fermée'
```

A vous de jouer !

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


## Ecrire dans un fichier CSV


La librairie [`csv`](https://docs.python.org/fr/3/library/csv.html) de Python sert aussi à écrire des fichiers CSV.


## Exemple d'écriture d'un CSV avec Python

```python
import csv

data = [
  [ "avril", 1 ],
  [ "mai", 4 ],
  [ "juin", 3 ]
]

with open('test.csv', "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in data:
        writer.writerow(line)
```

### Exercice: Exporter les morceaux durant moins d'une minute vers un fichier CSV

Vous allez maintenant devoir exporter toutes les chansons de moins d'une minute contenues dans la base de données Chinook vers un fichier CSV.


```python
import csv
import sqlite3

conn = sqlite3.connect('chinook.db')
print 'Database connectée'

# 1. read data from database

# 2. write CSV file

```

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
