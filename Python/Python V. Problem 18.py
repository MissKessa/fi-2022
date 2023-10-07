#Python V. Problem 18
import utils

def line(ch, n):
    """Returns a string with n characters ch"""
    return n * ch


def interior_line(ch, n):
    """Returns a string with n characters ch only in the borders"""
    result=""
    for j in range (0,n,1):
        if j==0 or j==n-1:
            result+=ch
        else:
            result+=" "
    return result


def square(ch,n):
    """Returns a square with n lines and character ch"""
    for i in range (0,n,1):
        print(line (ch,n))


def outlineSquare(ch,n):
    """Returns a square with n lines and character ch with the inside empty"""
    for i in range (0,n,1):
        if i==0 or i==n-1:
            print(line (ch,n))
        else:
            print(interior_line(ch,n))


ch=input("Write the character: ")
n=utils.read_positive_integer("How many times you want to repeat it? ")
outlineSquare(ch,n)