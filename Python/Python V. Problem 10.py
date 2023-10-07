#Python V. Problem 10
import utils

def calculate_proper_divisors(a):
    """This function calculates the sum of all the divisors of a number 
    and they are different than that number"""
    sum_divisors=0
    for i in range(1,a,1):
        if a%i==0:
            sum_divisors+=i
    return(sum_divisors)

            
def is_perfect_number(b):
    """This function returns True if the number is a perfect number 
    (the sum of it's divisor is equal to the number)"""
    if calculate_proper_divisors(b)==b:
        return True
    return False


number=utils.read_positive_integer("Write a positive number: ")
if is_perfect_number(number):
    print("It's a perfect number")
else:
    print("It's not a perfect number")