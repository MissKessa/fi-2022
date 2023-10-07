#Python VI. Problem 16
import utils
import random

def generate_vector(n,beg,end):
    """It generates a random vector with n elements"""
    p=[]
    while n>0:
        p.append(random.randint(beg,end))
        n-=1
    return p

n=utils.read_positive_integer("How many elements has the list? ")
a=utils.read_integer("Write the beginning of the randoms: ")
b=utils.read_integer("Write the end of the randoms: ")

print(generate_vector(n,a,b))



