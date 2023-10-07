#Python VI. Problem 9
import utils

def rotate_left(p):
    """Given a list of ints any length,
    return a list with the elements 'rotated left'
    (the position move one to the left)"""
    rotated=p[:]
    first_element=rotated.pop(0)
    rotated.append(first_element)
    return rotated

character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)

print("The rotated left list is", rotate_left(list1))