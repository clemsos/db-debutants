# Construire une application de base de données


## Le Musée de la Chaussure

Notre objectif pour la suite du cours : construire un système d'information pour le [Musée de la Chaussure](https://www.museedelachaussure.fr/).

![](https://4.bp.blogspot.com/-6wOGSeo4sx0/Vrd1FyFBN7I/AAAAAAAAFPk/Zefp4GC2W9Y/s1600/z.musee_.chaussure.romans.jpg)

### Les étapes de la conception à la réalisation

Pourquoi concevoir une application ?  
Listons ensemble les étapes

### Construire un prototype

Pourquoi réaliser un prototype ?  
Python et SQLite

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
