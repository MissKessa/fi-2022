#Python VI. Problem 15
import utils

def max(v1,v2):
    """Return the larger of 2 values"""
    if v1>v2:
        return v1
    return v2


def popular_name(p):
    """It returns the more popular name in a list"""
    names=p[0:len(p):2]
    numbers=p[1:len(p):2]
    for i,number in enumerate(numbers):
        if i==0:
            maximum=number
            position=i
        if number>maximum:
            position=i
            maximum=number
    return names[position]
    
    

character=input("what separator are you going to use? ")
list1=utils.read_list_some_integers("Write a list: ",character,1,2)

print("The most popular name is",popular_name(list1))