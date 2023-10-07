#Python VI. Problem 19
import statistics 
import random

def generate_uniform_vector(n):
    """It generates a random vector with n elements"""
    p=[]
    while n>0:
        p.append(round(random.random(),3))
        n-=1
    return p


def calculate_stadistic(p):
    """Computes the mean and the standard deviation"""
    average=statistics.mean(p)
    standard_deviation=statistics.stdev(p)
    return average,standard_deviation


def eliminate_out_of_range(p):
    """Each value in the vector out of the interval [average-standard_deviation; average+standard_deviation] should be assigned a 0."""
    q=p[:]

    average,standard_deviation=calculate_stadistic(q)
    lower_limit=average-standard_deviation
    upper_limit=average+standard_deviation
    for i in range (0,len(p),1):
        if q[i]<lower_limit or q[i]>upper_limit:
            q[i]=0
    return q


vector=generate_uniform_vector(15)
print("The original vector is:",vector)
print("The new vector is:",eliminate_out_of_range(vector))