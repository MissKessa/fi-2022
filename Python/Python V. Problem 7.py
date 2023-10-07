#Python V. Problem 7
import math
import utils

def distance_to_origin(x,y):
    """This function returns the distance between a point with 2 coordinates an the origin"""
    return math.sqrt(x**2+y**2)

x=utils.read_float("Write the x coordinate: ")
y=utils.read_float("Write the y coordinate: ")
distance=distance_to_origin(x,y)
print("The distance to the origin is",distance)