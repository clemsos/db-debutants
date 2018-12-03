import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

def insert_record(_name, _year, _stars):
    cmd ='''INSERT INTO shoes(NAME,YEAR,STARS) VALUES("%s",%s,%s)'''%(_name, _year, _stars)
    print cmd
    db.execute(cmd)

    db.commit()
    print 'Record inserted'

insert_record('Adidas Stan Smith', 1963 ,4)

db.close()
print ' Database Closed'
