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