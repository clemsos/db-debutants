# Importer / Exporter des données

## Révisions du vocabulaire

Qu'avons-nous utilisé ?

- programmes
- languages
- concepts / mots nouveaux

## Lire un fichier CSV

Vous trouverez tous ces exemples dans le dossier [`./music`](https://github.com/clemsos/db-debutants/tree/master/music)

### Le fichier de données

Nous allons utiliser [un échantillon](https://think.cs.vt.edu/corgis/csv/music/music.html) du Million Song Dataset.

Comment est-t-il structuré (headers, séparateurs, etc.)

## Lire un fichier CSV

La librairie [`csv`](https://docs.python.org/fr/3/library/csv.html) de Python sert à lire des fichiers de données.

### Compter le nombre de lignes dans le fichier

```python
import csv

with open('music.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1

print "Il y a %s lignes dans ce fichier"%line_count
```

Le fichier CSV nommé `music.csv` contient 10000 enregistrements.

## Importer un CSV dans une base de données

Nous allons maintenant importer le fichier `music.csv` dans la base de données `chinook.db` en utilisant un script Python.

### Les étapes

Voici les étapes :

1. télécharger le [jeu de données](https://think.cs.vt.edu/corgis/csv/music/music.html)
2. lire les partie intéressantes (chansons, auteurs, titres d'albums)
3. les inscrire dans notre base de données.

### Exercice : importer les artistes du CSV dans Chinook

A vous de jouer !

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

## Construire un modèle SQL

Objectif

- Lire des données existentes
- Imaginer un schéma
- Comprendre les relations entre des données


### Exercice : ajouter les concerts au systèmes Chinook

Chinook commence à vendre des billets de concerts et ainsi à désormais besoin de stocker ces informations.

Vous allez devoir **concevoir la partie du système chargée de la gestion des concerts**, nouvelle fonctionnalité s'ajoute de la base de données Chinook déjà existante.

Vous allez utiliser les informations déjà existantes dans Chinook pour rendre la recherche de concerts plus faciles (artistes).

Les concerts sont disponibles sous la forme de listes :

```csv
tel,name,artist,adresse,time,date
05.62.17.54.06,CITRON BLEU,Barbara Jones,66 RUE DES PARADOUX,19:30,01/19/2017
05 61 20 52 20,LES METS'TISSES,Madonna,37 RUE DENIS PAPIN,18:30,01/01/2018
05 61 21 24 67,LE CHAMPAGNE,Barbara Jones,3 RUE PEYRAS,18:00,01/04/2018
05 61 57 96 95,REST'O JAZZ,The Fabulous Thunderbirds,26 RUE AMELIE,18:00,12/14/2016
05 61 20 52 20,LES METS'TISSES,Madonna,37 RUE DENIS PAPIN,18:30,01/01/2018
05 61 14 23 16,DUBLINERS,Barbara Jones,32 AV MARCEL LANGER,18:00,05/23/2017
05 61 42 02 22,LE CARSON CITY,The Fabulous Thunderbirds,62 PL OLIVIER,18:00,12/23/2018
05 61 21 68 81,LE CACTUS,Mira,16 BD LASCROSSES,20:30,04/03/2018
05 61 25 78 31,LE VENT DU SUD,Mira,52 AV DE LESPINET,18:00,12/20/2018
05 61 21 92 18,CAFE ROCK LE DAUPHIN,Mira,11 BD DE STRASBOURG,18:30,12/31/2017
```

Vous trouverez ici un [échantillon de concerts](https://github.com/clemsos/db-debutants/raw/master/music/gigs.csv).


Ce que vous devez faire :

- décrire le schéma le plus adapté pour stocker les concerts
- créer ce schéma en SQLite
- importer l'échantillon de concerts dans votre base


A vous de jouer !
