# Let be a cylindrical swimming pool. Its diameter is 10m and its depth is 4m.
# It is filled with water from a tap capable of giving a stream of 80 liters per minute. 
# How many hours it takes to be filled?

# First, calculate the volume in liters

# The formula is: radio (in meters) **2 * PI * depth(in meters) 
# And then, change to liters multiplying by 1000
import math
volume = (10**2) * math.pi * 4 * 1000 #volume = 10***2.... *** is not an operator
                              #.. * PI * 4 * 100  PI is a method in the math class, so uoy must import math and then call the method

# Second, calculate how many minutes it takes to be filled
# The formula is: the total volume of the swimming pool / stream

minutes = volume / 80 #minutes = volumenn / 80 The variable is called volume

# Show the time in hours
print (round(minutes/60,2)) #print round(minutes/60,2) The parenthesis of print
