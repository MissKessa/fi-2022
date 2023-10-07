#Python II. Problem 2
import math
size_1= float(input("Write the first small size of the triangle as a real number: "))
size_2= float(input("Write the second the small size of the triangle as a real number: "))

large_size=math.sqrt((size_1**2)+(size_2**2))

print("The large size of the triangle is",large_size)