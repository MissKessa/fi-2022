#Python VI. Problem 7
import utils

def write_zeros(p):
    """Receives a list and change all negative numbers in the list by zero.
    The function will return an integer indicating how many changes you have made"""
    counter=0
    for i in range (0,len(p),1):
        if p[i]<0:
            p[i]=0
            counter+=1
    return counter


character=input("what separator are you going to use? ")
list2=utils.read_list_integers("Write a list: ",character)

print("The new list is",list2,". Number of changes:",write_zeros(list2))