#Python V. Problem 14
import utils

def is_in_range(number,beg,end):
    """This function returns True if the number is in the range [beg,end]"""
    if number>=beg and number<=end:
        return True


beg_1=utils.read_positive_integer("Write the beginning of the range: ")
end_1=utils.read_positive_integer("Write the end of the range: ")

beg_2=utils.read_positive_integer("Write the beginning of the other range: ")
end_2=utils.read_positive_integer("Write the end of the other range: ")

for i in range (beg_1,end_1+1,1):
    if is_in_range(i,beg_2,end_2):
        print(i)