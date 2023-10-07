#Python VI. Problem 10
import utils

def first_last6(p):
    """Given a list of ints, return True if 6 appears as either the first or last element
in the list"""
    if p[0]==6 or p[-1]==6:
        return True
    return False


character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)

print("Does the list have a 6 on the first or last element?",first_last6(list1))