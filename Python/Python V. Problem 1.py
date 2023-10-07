#Python V. Problem 1
import utils

def biggest(number1,number2):
    """Given two numbers, returns the biggest"""
    if number1>=number2:
        return number1
    else:
        return number2


a=utils.read_integer("Write an integer: ")
b=utils.read_integer("Write another integer: ")
biggest_number=biggest(a,b)
print("The biggest number is",biggest_number)
#the standard is 2 lines between functions
