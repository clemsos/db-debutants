import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

data = [
    { "name" : "chaussure indienne", "year" : -3300, "stars" : 0 },
    { "name" : "chaussure chinoise", "year" : -1200, "stars" : 0 },
    { "name" : "chaussure perse", "year" : 100, "stars" : 0 }
]

def insert_record(_name, _year, _stars):
    cmd ='''INSERT INTO shoes(NAME,YEAR,STARS) VALUES("%s",%s,%s)'''%(_name, _year, _stars)
    print cmd
    db.execute(cmd)

    db.commit()
    print 'Record inserted'

for chaussure in data :
    insert_record(chaussure["name"], chaussure["year"], chaussure["stars"])

db.close()
print ' Database Closed'
