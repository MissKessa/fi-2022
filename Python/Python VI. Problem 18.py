#Python VI. Problem 18
import utils
import random

def generate_vector(n,beg,end):
    """It generates a random vector with n elements"""
    p=[]
    while n>0:
        p.append(random.randint(beg,end))
        n-=1
    return p


def count_votes(p):
    """Counts the votes of each partie.
    -1 == invalid
    0 == blank
    1 == valid """
    invalid=0
    blank=0
    valid=0
    for i in p:
        if i==-1:
            invalid+=1
        elif i==0:
            blank+=1
        else:
            valid+=1
    return invalid,blank,valid



def print_results(name,p):
    """Prints the results of a party in percentages"""
    invalid,blank,valid=count_votes(p)
    print(name,"has:")
    print("Invalid",round(invalid/15*100),"%")
    print("Blank",round(blank/15*100),"%")
    print("Votes",round(valid/15*100),"%")
    print()


party1=generate_vector(15,-1,1)
party2=generate_vector(15,-1,1)
party3=generate_vector(15,-1,1)
party4=generate_vector(15,-1,1)
party5=generate_vector(15,-1,1)

print_results("Party 1",party1)
print_results("Party 2",party2)
print_results("Party 3",party3)
print_results("Party 4",party4)
print_results("Party 5",party5)

