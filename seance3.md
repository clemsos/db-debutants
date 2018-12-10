# Importer / Exporter des données

## Révisions du vocabulaire

- quels programmes avons-nous utilisés?
- quels concepts / mots nouveaux ?


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

## Exercice: Exporter les morceaux durant moins d'une minute vers un fichier CSV

Vous allez maintenant devoir exporter toutes les chansons de moins d'une minute contenues dans la base de données Chinook vers un fichier CSV.


```python
import csv
import sqlite3

conn = sqlite3.connect('chinook.db')
print 'Database connectée'

# 1. read data from database

# 2. write CSV file

```
