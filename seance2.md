# Construire une application de base de données


## Petites révisions

Promenons-nous grâce à une interface graphique : [SQLite Browser](https://sqlitebrowser.org/).

![](https://github.com/sqlitebrowser/sqlitebrowser/raw/master/images/sqlitebrowser.png)

## Le Musée de la Chaussure

Notre objectif pour la suite du cours : construire un système d'information pour le [Musée de la Chaussure](https://www.museedelachaussure.fr/).

![](https://4.bp.blogspot.com/-6wOGSeo4sx0/Vrd1FyFBN7I/AAAAAAAAFPk/Zefp4GC2W9Y/s1600/z.musee_.chaussure.romans.jpg)

### Les étapes de la conception à la réalisation

Pourquoi concevoir une application ?  
Listons ensemble les étapes

### Construire un prototype

Pourquoi réaliser un prototype ?  
Python et SQLite

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

### Définir un schéma

#### sqlite
```sql
sqlite> CREATE TABLE Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT);
```

#### Python sqlite3

```python
import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('CREATE TABLE Users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)')

```

#### Python Peewee (autre librairie)

```python
from peewee import *

db = SqliteDatabase('users.db')

class User(Model):
	username = TextField()
	email = CharField(max_length=255, unique=True)

db.create_tables([User], safe=True)
```

## Enoncé: le prototype du catalogue du Musée de la Chaussure

### L'objectif

Vous devez produire un schéma de base de données pour le catalogue du [Musée de la Chaussure](https://www.museedelachaussure.fr). Ce schéma fait partie de l'application utilisée par les gestionnaires du musée.

L'application doit permettre de :

- lire des infos détaillées sur chaque pièce
  - titre
  - époque, provenance
  - photo
  - etc.
- localiser la pièce dans les collections
  - nom de la collection
  - emplacement physique (allée, étagère, etc)
- connaître le status actuel de l'inventaire
  - pièce exposée
  - prétée
  - en réparation
  - etc.
- constituer ou consulter des listes d'oeuvres (notamment pour les expositions)

### Comment faire ?

Vous devez

1. définir le modèle conceptuel sur lequel reposera votre schéma (structure, terminologie, etc)
2. utiliser une base de données SQL pour constuire un prototype de votre modèle
3. présenter vos résultats au musée.

### Quels outils sont les plus adaptés?

Il existe de très nombreux outils pour construire des schémas SQL (logiciels, appli en ligne, etc ) répondant aux besoins multiples de conception d'application possédant des bases de données.

Pour cette fois, commençons avec quelque chose de simple :

1. le schéma : papier + crayon
2. bases de données et modèle : Python + SQlite
3. constuire des exemples de requête
