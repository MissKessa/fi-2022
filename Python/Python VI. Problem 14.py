#Python VI. Problem 14
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


def search_min_max(p):
    """It returns the maximum and minimun of a list"""
    minimum=0
    maximum=0
    for i in range(0,len(p),1):
        if i==0:
            minimum=min(p[i],p[i+1])
            maximum=max(p[i],p[i+1])
        minimum=min(minimum,p[i])
        maximum=max(maximum,p[i])
    return minimum,maximum

def centered_average(p):
    """Return the "centered" average of a list of ints, which we’ll say is the mean
average of the values, except ignoring the largest and smallest values in the list. If there
are multiple copies of the smallest value, ignore just one copy, and likewise for the largest
value"""
    q=p[:]
    minimum,maximum=search_min_max(p)
    q.remove(minimum)
    q.remove(maximum)

    summation=0
    counter=0
    for i in q:
        summation+=i
        counter+=1
    return summation//counter
#sum and counter=len(p)

character=input("what separator are you going to use? ")
list1=utils.read_list_of_length("Write a list: ",character,3)

print("The centered average is",centered_average(list1))