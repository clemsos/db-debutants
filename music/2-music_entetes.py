import csv

with open('music.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0 :
            print row # la premiere colonne
            print "--"*10
            for entete in row :
                print entete

        line_count = line_count +1
