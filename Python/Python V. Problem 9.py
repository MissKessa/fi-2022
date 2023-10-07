#Python V. Problem 9
import utils

def calculate_semifactorial(a):
    """This function returns the semifactorial of a given number"""
    semifactorial=1
    while a>1:
        semifactorial*=a
        a-=2
    return semifactorial


number=utils.read_positive_integer("Introduce a number: ")
semifactorial=calculate_semifactorial(number)
print("The semifactorial is",semifactorial)