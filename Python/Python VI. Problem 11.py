#Python VI. Problem 11
import utils

def reverse(p):
    """Given a list of ints any length,
    return a list in inverse order"""
    reverse=p[:]
    for i in range(0,len(p),1):
        reverse[i]=p[-i-1]
    return reverse

character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)

print("The reverse list is", reverse(list1))