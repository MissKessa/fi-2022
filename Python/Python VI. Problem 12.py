#Python VI. Problem 12
import utils

def count_evens(p):
    """ Return the number of even ints in the given list."""
    counter=0
    for i in p:
        if i%2==0:
            counter+=1
    return counter

character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)

print("The number of even numbers is:",count_evens(list1))