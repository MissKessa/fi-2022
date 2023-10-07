#Python II. Problem 1
height= float(input("Write the height as a real number: "))
base= float(input("Write the base as a real number: "))
area=base*height/2

#print("The area of a triangle with base "+ base +
    #" and height "+ height +
    #" is "+ area)

#Way 1. Print with commas transform the variables to string automatically
print("The area of a triangle with base",base,
    "and height", height,
    "is",area)

#Way 2
print("The area of a triangle with base ",str(base),
    " and height ", str(height),
    " is ", str(area))