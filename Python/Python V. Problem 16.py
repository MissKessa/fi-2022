#Python V. Problem 16
import utils

def transform_digit(digit):
    """Transforms the digit into a string if it's less than 10
    and if it's greater than 10 we transform it to the letter corresponding to the basis higher than 10"""
    if digit==11:
        return "A"
    elif digit==12:
        return "B"
    elif digit==13:
        return "C"
    elif digit==14:
        return "D"
    elif digit==15:
        return "E"
    return str(digit)


def calculate_number_in_base(number,base):
    """Calculates a given number in a given base.
    It returns a string"""
    result=""
    while number>0:
        digit=number%base
        result+=transform_digit(digit)
        number=number//base
    return result[::-1]


n=utils.read_positive_integer ("Write the number you want to convert: ")
#b=utils.read_in_range_integer("Write the base: ",2,16)

print(n,"in base",2,"is",calculate_number_in_base(n,2))
print(n,"in base",8,"is",calculate_number_in_base(n,8))
print(n,"in base",10,"is",calculate_number_in_base(n,10))
print(n,"in base",16,"is",calculate_number_in_base(n,16))