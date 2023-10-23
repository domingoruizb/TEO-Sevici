import csv
import math
from collections import namedtuple

Coordinates = namedtuple('Coordinates', 'latitude, longitude')
Station = namedtuple('Station', 'name, slots, empty_slots, free_bikes, location')


def read_stations(fileName):
    with open(fileName, encoding = "utf-8" ) as f:
        lector = csv.reader(f)
        next(lector)
        output_list = []
        for name, slots, empty_slots, free_bikes, latitude, longitude in lector: 
            slots = int(slots)
            empty_slots = int(empty_slots)
            free_bikes = int(free_bikes)
            latitude = float(latitude)
            longitude = float(longitude)
            c = Coordinates(latitude, longitude)
            output_list.append(Station(name, slots, empty_slots, free_bikes, c))
        return output_list
    
#exercise 2.1
def free_bikes_stations(station, k=5):
    return sorted([(s.free_bikes, s.name) for s in station if s.free_bikes >= k], reverse = True)

#exercise 2.2

def distance_locations(c1, c2):
    return float(math.sqrt(((c1.latitude - c2.latitude) ** 2) + ((c1.longitude - c2.longitude) ** 2)))

def nearest_stations(stations, location, k=5):
    nearest_st =sorted([(distance_locations(station.location, location), station.name, station.free_bikes) for station in stations])
    return sorted(nearest_st[:k], reverse = True, key = lambda t:t[2]) #lambda recieves t and return t[2] 
    #key is a function parameter (nt 4)


#exercise 4 HW
def mean_coordinates(stations):
    fb_coord = [s.location for s in stations if s.free_bikes >= 5]
    return sum(fb_coord[0])/len(fb_coord[0]), sum(fb_coord[1])/len(fb_coord[1])
    
'''

'''




