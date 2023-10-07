#Python VI. Problem 6
import utils

def biggest_element(p):
    """Returns the index (position) of the largest element
of the list"""
    for i in range(0,len(p),1):
        if i==0:
            maximum=p[i]
            position=i
        if p[i]>maximum:
            maximum=p[i]
            position=i
    return position

character=input("what separator are you going to use? ")
list2=utils.read_list_integers("Write a list: ",character)
print("The position of the biggest element of the list is",biggest_element(list2))