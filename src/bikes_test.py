from bikes import * 

def main():
    my_stats = read_stations("./TEO-Sevici/data/estaciones.csv")
    print(f"There are {len(my_stats)} stations")
    test_free_bikes_stations(my_stats)
    #ex 2.2
    c = Coordinates(37.357659, -5.9863)
    print("5 stations nearest to me: ")
    print(nearest_stations(my_stats, c))
    print("2 stations nearest to me: ")
    print(nearest_stations(my_stats, c))
    print("The total mean coordinates are: ", mean_coordinates(my_stats))

    my_map = create_map_stations(my_stats, lambda s: "blue")
    save_map(my_map, "./TEO-Sevici/out/blue.html")

    #create a map with:
    #red markers for stations without free bikes
    #green markers for stations with free bikes
    my_map2 = create_map_stations(my_stats, color_free_bikes_station)
    save_map(my_map2, "./TEO-Sevici/out/free_bikes.html")

    #create a map with:
    # red markers for stations without free slots
    # blue markers for stations with free slots
    my_map3 = create_map_stations(my_stats, color_free_slots_stations)
    save_map(my_map3, "./TEO-Sevici/out/free_slots.html")


#ex 2.1
def test_free_bikes_stations(station):
    print("There are ", len(free_bikes_stations(station, 5))," with 5 or more free bikes and the firsts 3 are: ")
    print(free_bikes_stations(station, 5)[:3])
    print("There are ", len(free_bikes_stations(station, 10))," with 10 or more free bikes and the firsts 3 are: ")
    print(free_bikes_stations(station, 10)[:3])
    print("There are ", len(free_bikes_stations(station, 1))," with 1 or more free bikes and the firsts 3 are: ")
    print(free_bikes_stations(station, 1)[:3])



if __name__ == "__main__":
    main()