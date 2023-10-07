#Python V. Problem 5
import utils

def read_mark(message):
    while True:
        number=utils.read_positive_integer(message)
        if number<=10:
            return number
        print("The mark must be lower or equal to 10")


def write_mark(mark):
    """This function returns a number depending on the mark.
    -returns 1 when the mark is "F" (mark between [0,5))
    -returns 2 when is "E" ([5,6))
    -returns 3 when is "D" ([6,7))
    -returns 4 when is "C" ([7,8))
    -returns 5 when is "B" ([8,9))
    -returns 6 when is "A" ([9,10))
    -returns 7 when is "A+" (10)"""
    if mark<5:
        return 1
    elif mark<6:
        return 2
    elif mark<7:
        return 3
    elif mark<8:
        return 4
    elif mark<9:
        return 5
    elif mark<10:
        return 6
    else:
        return 7


mark=read_mark("Write the mark of a student: ")
letter=write_mark(mark)
if letter==1:
    print("The mark is F")
elif letter==2:
    print("The mark is E")
elif letter==3:
    print("The mark is D")
elif letter==4:
    print("The mark is C")
elif letter==5:
    print("The mark is B")
elif letter==6:
    print("The mark is A")
else:
    print("The mark is A+")

#check eval() to see if the input is atype