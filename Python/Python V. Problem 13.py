#Python V. Problem 13
import utils

def is_in_range(number,beg,end):
    """This function returns True if the number is in the range [beg,end]"""
    if number>=beg and number<=end:
        return True


number=utils.read_positive_integer("Write a number: ")
beginning=utils.read_positive_integer("Write the beginning of the range: ")
end=utils.read_positive_integer("Write the end of the range: ")
if is_in_range(number,beginning,end):
    print("The number is in range")
else:
    print("The number is not in range")