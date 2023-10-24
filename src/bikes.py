import csv
import math
from collections import namedtuple
from maps import *

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
    list_lat = []
    list_long = []
    for s in stations:
        lat = s.location.latitude
        list_lat.append(lat)
        long = s.location.longitude
        list_long.append(long)
    mean_lat = sum(list_lat)/len(list_lat)
    mean_long = sum(list_long)/len(list_long)
    return Coordinates(mean_lat, mean_long)
    

def create_map_stations(stations, function_color):
    map_centre = mean_coordinates(stations)
    map = crea_mapa(map_centre[0], map_centre[1], 13)
    for s in stations:
        etiqueta = s.name
        color = function_color(s)
        marker = create_marker(s.location[0], s.location[1], etiqueta, color)
        marker.add_to(map)
    return map

def color_free_bikes_station(station):
    if station.free_bikes >= 1:
        return "green"
    else:
        return "red"
    
def color_free_slots_stations(station):
    if station.empty_slots >=1:
        return "blue"
    else:
        return "red"







