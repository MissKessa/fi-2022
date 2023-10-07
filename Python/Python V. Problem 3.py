#Python V. Problem 3
import utils

def biggest(number1,number2):
    """Given two numbers, returns the biggest"""
    if number1>=number2:
        return number1
    else:
        return number2


a=utils.read_integer("Write an integer: ")
b=utils.read_integer("Write another integer: ")
c=utils.read_integer("Write the last integer: ")
biggest_number=biggest(biggest(a,b),c)
print("The biggest number is",biggest_number)
#the standard is 2 lines between functions
