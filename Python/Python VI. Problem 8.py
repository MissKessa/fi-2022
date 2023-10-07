#Python VI. Problem 8
import utils

def sum_powers(l,power):
    """ This function should calculate the value of each item in the list to the power
of n and add all them, returning the result"""
    sum_elements=0
    for i in range (0, len(l),1):
        sum_elements+=l[i]**power
    return sum_elements

character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)
n=utils.read_float("Write a number: ")

print("The sum of the elements^n is",sum_powers(list1,n))