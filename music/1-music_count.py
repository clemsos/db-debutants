import csv

with open('music.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count = line_count + 1

print "Il y a %s lignes dans ce fichier"%line_count
