#Python V. Problem 15
import utils


def calculate_element_n (b,c,d,k):
    """Calculates the nth element of this series"""
    if k==0:
        return b
    return c*calculate_element_n(b,c,d,k-1)+d


b=utils.read_integer("Write the element b: ")
c=utils.read_integer("Write the element c: ")
d=utils.read_integer("Write the element d: ")
k=utils.read_positive_integer("Write the position that you want to calculate: ")
element=calculate_element_n(b,c,d,k)
print("The element",k,"is",element)