#Python 3. Problem 13
import numbers
import random
a=float(input("Write a number between 0 and 1: "))
random_number=random.uniform(0,1)

if random_number>a:
    print("The dragon have eaten you")
else:
    print("You are free")