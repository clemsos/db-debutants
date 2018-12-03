import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

def read_data():
    # from math import *
    data = db.execute(''' SELECT * FROM shoes ORDER BY NAME''')
    for record in data:
        print 'ID : '+str(record[0])
        print 'NAME : '+str(record[1])
        print 'YEAR : '+str(record[2])
        print 'STARS : '+str(record[3])+'\n'


read_data()

db.close()
print ' Database Closed'
