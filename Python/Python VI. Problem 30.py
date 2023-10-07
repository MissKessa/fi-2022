#Python VI. Problem 30

def metamorphosis(a):
    """Converting from a string
to any valid data type among the following:
-integer: just containing digits plus leading and ending spaces,
-bool: True or False plus leading and ending spaces,
-float: digits+dot+digits format, allowing ' 23.4 ', ' .234 ' and ' 234.' as valid floats,
-str: the remaining cases it is just a string"""
    a=a.strip()
    if a.isdigit():
        return int(a)
    elif a=="True" or a=="False":
        return bool(a)
    elif a.replace(".","",1).isdigit():
        return float(a)
    return a

b=input("Write something: ")
print(metamorphosis(b))
print(type(metamorphosis(b)))