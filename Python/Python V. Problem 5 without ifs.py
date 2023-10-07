#Python V. Problem 5 without ifs
def read_float(message):
    """This function returns a float value requested to the user with 
    a suitable message using standard input.
    If the user enter a number out of [0,10], it wil ask again"""
    while True:
        number=input(message)
        if number.lstrip("-").isdigit():
            number=int(number)
            if number>=0 and number<=10:
                return number


def write_mark(mark):
    """This function returns a number depending on the mark."""
    return chr(mark)


mark=read_float("Write the mark of a student: ")
letter=write_mark(mark)
print(letter)