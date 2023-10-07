#Python VI. Problem 17
import utils

def write_list_by_columns(p,columns):
    """Given a vector of real numbers, prints the values in m
columns."""
    for i in range (0,len(p)):
        if (i)%columns==0:
            print()
        print(p[i], end=" ")


character=input("what separator are you going to use? ")
list1=utils.read_list_some_floats("Write a list: ",character,0,1)
m=utils.read_positive_integer("Write a number: ")

write_list_by_columns(list1,m)