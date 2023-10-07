#Python VI. Problem 13
import utils

def min(v1,v2):
    """Return the smaller of 2 values"""
    if v1<v2:
        return v1
    return v2


def max(v1,v2):
    """Return the larger of 2 values"""
    if v1>v2:
        return v1
    return v2


def big_diff(p):
    minimum=0
    maximum=0
    for i in range(0,len(p),1):
        if i==0:
            minimum=min(p[i],p[i+1])
            maximum=max(p[i],p[i+1])
        minimum=min(minimum,p[i])
        maximum=max(maximum,p[i])
    return maximum-minimum


character=input("what separator are you going to use? ")
list1=utils.read_list_integers("Write a list: ",character)

print("The difference between the minimum and the maximum is",big_diff(list1))