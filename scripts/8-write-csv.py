# -*- coding: utf-8 -*-
import csv

data = [
  [ "avril", 1 ],
  [ "mai", 4 ],
  [ "juin", 3 ]
]

with open('test.csv', "wb") as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow([ "Mois", "Quantité"])
    for line in data:
        writer.writerow(line)
