import csv
import random

import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)


artists = []
with open('music.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        artists.append(row[2])

lieux = []
with open('cafes-concerts.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')

    for row in csv_reader:
        lieux.append({
            "name" : row[2],
            "tel" : row[4],
            "adresse" : "%s %s"%(random.randint(0, 70), row[9])
        })

def get_gigs(_count) :
    gigs = []
    for row in range(0, _count):
        gig = random.choice(lieux)
        gig["date"] = randomDate("1/1/2016", "2/1/2019", random.random())
        half_hour =["00", "30"]
        gig["time"] = "%s:%s"%(random.randint(18,22), random.choice(half_hour))
        gigs.append(gig)
    return gigs

data = []

for i in range(0,10):
    artist = random.choice(artists)
    gigs = get_gigs(random.randint(1,10))
    for gig in gigs:
        gig["artist"] = artist
        data.append(gig)

print data

keys = data[0].keys()

with open('gigs.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)
