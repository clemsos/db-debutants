import sqlite3

# Open a database file
db = sqlite3.connect('shoes_test.db')
print 'Database opened'

db.close()
print 'Database closed'
