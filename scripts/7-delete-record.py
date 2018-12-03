import sqlite3

db = sqlite3.connect('shoes_test.db') # Open a database File
print 'Database opened'

def delete_record():
    db.execute(''' DELETE from shoes WHERE ID = 1 ''')
    db.commit()
    print 'Deleted'

delete_record()
print '----------------------'

db.close()
print ' Database Closed'
