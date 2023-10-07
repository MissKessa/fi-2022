#Python V. Problem 20
import utils

def fibonacci(n):
    """Calculates the nth element of the fibonacci series"""
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


def sum_fibonnaci(m):
    sum=0
    for k in range (1,m+2,1):
        sum+=fibonacci(k)
        print(sum,end=" ")


a=utils.read_positive_integer("What element you want to calculate: ")
sum_fibonnaci(a)