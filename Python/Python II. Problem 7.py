#Python II. Problem 7
distance_meters= float(input("Write a distance in meters:"))
distance_yards=round(distance_meters*1.0936,4)
distance_feet=round(distance_meters* 3.2808,4)
distance_inches=round(distance_meters* 39.370,4)
print("The distance is",distance_meters,"m")
print("The distance is",distance_yards,"yd")
print("The distance is",distance_feet,"ft")
print("The distance is",distance_inches,"in")