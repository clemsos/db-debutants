import csv
import sqlite3

conn = sqlite3.connect('example.db')
print 'Database connectée'

with open('music.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        artist_name = row[2]

    # insert artist name into artists tables


db.close()
print 'Database fermée'
