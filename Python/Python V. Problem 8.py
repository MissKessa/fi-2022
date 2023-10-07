#Python V. Problem 8
import math
import utils

def length_circle(x,y):
    """This function returns the length of a circle whose center is the origin and passes through a point """
    radius=x**2+y**2
    return 2*(math.pi)*radius

x=utils.read_float("Write the x coordinate: ")
y=utils.read_float("Write the y coordinate: ")
length=length_circle(x,y)
print("The length of the circle",round(length,4))