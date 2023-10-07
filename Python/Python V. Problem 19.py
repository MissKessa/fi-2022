#Python V. Problem 19
import utils


def fibonacci(n):
    """Calculates the nth element of the fibonacci series"""
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


n=utils.read_positive_integer("What element you want to calculate: ")
element=fibonacci(n)
print("The element",n,"is",element)