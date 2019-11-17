# Construire une application de base de données


## Petites révisions

Promenons-nous grâce à une interface graphique : [SQLite Browser](https://sqlitebrowser.org/).

![](https://github.com/sqlitebrowser/sqlitebrowser/raw/master/images/sqlitebrowser.png)


## Utiliser SQLite avec Python

### Python, un langage expressif

Voir des [exemples](https://wiki.python.org/moin/SimplePrograms) de programmes
Le [Zen de Python](https://www.python.org/dev/peps/pep-0020/)  

![](https://cdn-images-1.medium.com/max/1600/0*17G8RRzpccm_7F0U.png)

### Pourquoi écrire des scripts ?

Automatiser et être fainéant  
Différence entre un script et un programme

### Interagir avec une base de données

Structure d'un programme comprenant une base de données  
Les librairies


## Comment utiliser Python?

### En ligne de commande

```bash
$ python
Python 2.7.14 (default, Mar 22 2018, 14:43:05)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### Sous forme de fichier

Le fichier :
```python
# Fichier hello.py
print 'Hello, world!'
```

Executer avec Python
```bash
$ python hello.py
```

## Python et SQLite

### La librairie SQLite3

Page de documentation de la librairie [`sqlite3`](https://docs.python.org/2/library/sqlite3.html).

```python
import sqlite3
conn = sqlite3.connect('example.db')
```

### Quelques exemples

Vous trouverez dans le dossier [scripts](./scripts) les fichiers contenant ces différents exemples.

#### 1. Se connecter
```python
import sqlite3

# Open a database file
db = sqlite3.connect('shoes_test.db')
print 'Database opened'

db.close()
print 'Database closed'
```

#### 2. Créer une table

```python
db.execute(''' CREATE TABLE IF NOT EXISTS shoes(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    YEAR INT NOT NULL,
    STARS INT NOT NULL) ''')

print 'Table created'
```


#### 3. Insérer un enregistrement

```python
db.execute(''' INSERT INTO shoes(NAME,YEAR,STARS)
        VALUES('Adidas Stan Smith', 1963 ,4)
''')

db.commit()
print 'Record inserted'
```

#### 4. Insérer à partir d'une variable

```python
def insert_record(_name, _year, _stars):
    cmd ='''INSERT INTO shoes(NAME,YEAR,STARS) VALUES("%s",%s,%s)'''%(_name, _year, _stars)
    print cmd
    db.execute(cmd)

    db.commit()
    print 'Record inserted'

insert_record('Adidas Stan Smith', 1963 ,4)

```

Depuis un tableau de données

```python
data = [
    { "name" : "chaussure indienne", "year" : -3300, "stars" : 0 },
    { "name" : "chaussure chinoise", "year" : -1200, "stars" : 0 },
    { "name" : "chaussure perse", "year" : 100, "stars" : 0 }
]

for chaussure in data :
    insert_record(chaussure["name"], chaussure["year"], chaussure["stars"])
```

#### 5. Lire des données

```python
# from math import *
data = db.execute(''' SELECT * FROM shoes ORDER BY NAME''')

for record in data:
    print 'ID : '+str(record[0])
    print 'NAME : '+str(record[1])
    print 'YEAR : '+str(record[2])
    print 'STARS : '+str(record[3])+'\n'
```

#### 6. Mettre à jour un enregistrement

```python
def update_record(_id, _stars):
    db.execute(''' UPDATE shoes set STARS=%s WHERE ID=%s'''%(_stars, _id))
    db.commit()
    print 'Updated'

# Launch the update
update_record(3,50)
```
#### 7. Supprimer des enregistrements

```python
db.execute(''' DELETE from shoes WHERE ID = 1 ''')
  db.commit()
  print 'Deleted'
```

## Exercices : manipuler une base de données avec Python

Nous allons désormais utiliser Python pour manipuler la base de données Chinook du [cours précédent](./seance1).

```python
import sqlite3
conn = sqlite3.connect('chinook.db')
```

### Lire des données

Ecrire des scripts Python pour répondre aux questions précédentes :

- compter le nombre d'artistes
- compter combien de chansons qui dure moins de trois minutes
- afficher toutes les chansons d'un seul artiste
- compter le nombre de chansons de cet artiste


SUITE: Essayer maintenant d'[importer de nouvelles chansons depuis un fichier](/seance3)
