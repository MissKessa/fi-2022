#Python Utils: Useful functions
def read_integer(message):
    """This function returns an integer value requested to the user with 
    a suitable message using standard input."""
    while True:
        number=input(message)
        if number.lstrip("-").isdigit():
            return int(number) #works like a break
        print("Invalid number")


def read_float(message):
    """This function returns a float value requested to the user with 
    a suitable message using standard input"""
    while True:
        number=input(message)
        if number.lstrip("-").replace(".","",1).isdigit():
            return float(number)
        print("Invalid number")



def read_positive_integer(message):
    """This function returns a integer value requested to the user with 
    a suitable message using standard input.
    If the number is negative, the number is asked again"""
    while True:
        number=read_integer(message)
        if number>=0:
            return number
        print("The number must be positive")


def read_positive_float(message):
    """This function returns a float value requested to the user with 
    a suitable message using standard input.
    If the number is negative, the number is asked again"""
    while True:
        number=read_float(message)
        if number>=0:
            return number
        print("The number must be positive")


def read_greater_than_integer(message,beg):
    """This function returns a integer value if the number is greater than or equal to beg
    If not, the number is asked again"""
    while True:
        number=read_integer(message)
        if number>=beg:
            return number
        print("The number must be greater than or equal to",beg)


def read_in_range_integer(message,beg,end):
    """This function returns a integer value if the number is in the range [beg,end]
    If not, the number is asked again"""
    while True:
        number=read_integer(message)
        if number>=beg and number<=end:
            return number
        print("The number must be greater than or equal to",beg,"and less than or equal to",end)


def read_list(message,separator):
    list1=input(message)
    parts=list1.split(separator)
    return parts


#def read_list_integers(message,separator):
    #"""Reads a list split by the separator and checks if all the elements are integers.
    #If it's not a numeric list, it asks again for the list"""
    #while True:
        #parts=read_list(message,separator)        
        #numbers=[]

        #for i in range(0, len(parts),1):
        #    if parts[i].strip().lstrip("-").isdigit():
        #        numbers.append(int(parts[i])) #no modificando la lista
        #        continue
        
        #if len(numbers)==len(parts):
        #    return numbers
        #print("It's not a list of integers")


def read_list_integers(message,separator):
    """Reads a list split by the separator and checks if all the elements are integers.
    If it's not a numeric list, it asks again for the list"""
    while True:
        parts=read_list_some_integers(message,separator,0,1)        
        return parts


def read_list_some_integers(message,separator,beginning,step):
    """Reads a list split by the separator and checks if some elements are integers 
    (begining is the position, you start to check, and step what elements).
    If it's not a numeric list, it asks again for the list"""
    while True:
        parts=read_list(message,separator)
        numbers=[]
        for i in range (beginning,len(parts),step):
            if parts[i].strip().lstrip("-").isdigit():
                numbers.append(int(parts[i]))
                continue

        if len(numbers)==len(parts):
            return numbers
        print("Incorrect list")


def read_list_some_floats(message,separator,beginning,step):
    """Reads a list split by the separator and checks if some elements are floats 
    (begining is the position, you start to check, and step what elements).
    If it's not a numeric list, it asks again for the list"""
    while True:
        parts=read_list(message,separator)
        numbers=[]
        for i in range (beginning,len(parts),step):
            if parts[i].strip().lstrip("-").replace(".","",1).isdigit():
                numbers.append(float(parts[i]))
                continue

        if len(numbers)==len(parts):
            return numbers
        print("Incorrect list")


def read_list_of_length(message,separator,length):
    """Reads a list. If the length of the list is less than length, 
    it will be asked again"""
    while True:
        list1=read_list_integers(message,separator)
        if len(list1)>=length:
            return list1
        print("The length of list must be greater or equal to",length)