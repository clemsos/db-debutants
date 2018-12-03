import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

db.execute(''' INSERT INTO shoes(NAME,YEAR,STARS)
        VALUES('Adidas Stan Smith', 1963 ,4)
''')

db.commit()
print 'Record inserted'

db.close()
print ' Database Closed'
