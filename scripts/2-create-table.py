import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

db.execute(''' CREATE TABLE IF NOT EXISTS shoes(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    YEAR INT NOT NULL,
    STARS INT NOT NULL) ''')

print 'Table created'

db.close()
print ' Database Closed'
