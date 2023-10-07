#Python 3. Problem 5
a=int(input("Write a number: "))
print("a)Calculate the square of the number","b)Calculate the cube of the number","c)Calculate 2 times the number")
b=input("What option do you want? ")
if b=="a":
    print("The square of the number is:",a**2)
elif b=="b":
    print("The cube of the number is:",a**3)
elif b=="c":
    print("2 times the number is:",a*2)
else:
    print("You haven't chose the correct option")