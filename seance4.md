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
