#Python V. Problem 12
import utils

def is_prime(a):
    """This function returns True if the number is prime"""
    for i in range (1,a,1):
        if a%i==0 and not(i==1 or i==a):
            return False
    return True


while True:
    number=utils.read_integer("Write a number: ")
    if number<=0:
        break
    if is_prime(number):
        print(number,"is prime")
    else:
        print(number,"is not prime")
