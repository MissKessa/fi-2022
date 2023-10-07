#Python VI. Problem 24
import utils

def rotateleft(string,pos):
    """Given a string, return a 'rotated left x'
version where the first x chars are moved to the end. The string length will be at least 2.
or an error will raise."""
    if len(string)<2:
        return None
    return string[pos:len(string):1]+string[0:pos:1]


a=input("Write a word: ")
b=utils.read_positive_integer("Write how many positions do you want to rotate: ")

print(rotateleft(a,b))