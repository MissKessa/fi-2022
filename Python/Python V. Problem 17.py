#Python V. Problem 17
import utils

def line(ch, n):
    """Returns a string with n characters ch"""
    return n * ch


def square(ch,n):
    """Returns a square with n lines and character ch"""
    for i in range (0,n,1):
        print(line (ch,n))


ch=input("Write the character: ")
n=utils.read_positive_integer("How many times you want to repeat it? ")
square(ch,n)