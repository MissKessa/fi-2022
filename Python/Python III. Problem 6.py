#Python 3. Problem 6
a=int(input("Write the first mark in [0-100]: "))
b=int(input("Write the second mark in [0-100]: "))
c=int(input("Write the third mark in [0-100]: "))
d=int(input("Write the fourth mark in [0-100]: "))
average=(a+b+c+d)/4
if average<60:
    print("The average is E")
elif average<70:
    print("The average is D")
elif average<80:
    print("The average is C")
elif average<90:
    print("The average is B")
else:
    print("The average is A")