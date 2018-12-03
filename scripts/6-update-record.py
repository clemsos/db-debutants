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

# show data
read_data()

def update_record(_id, _stars):
    db.execute(''' UPDATE shoes set STARS=%s WHERE ID=%s'''%(_stars, _id))
    db.commit()
    print 'Updated'

# Launch the update
update_record(3,50)

print '----------------------'
read_data()


db.close()
print ' Database Closed'
