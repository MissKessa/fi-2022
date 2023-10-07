import math
# math operators and built-in functions (float with any number, gives the result as float)
print(2+3) #int+int=int
print("Hello"+"4") #Behaviour of operations change depending on the data type
print("Hello"*4)
print(2-3) #int-int=int
print(2*3) #int*int=int
print(4/2) #int/int=float
print (5//2) #get the integer part of the division. If one is a float, the integer will be as a float
print (5%2) #get the reminder of the division
print (5**2) #the power
print (max(5,2.3,10)) #returns the  biggest number
print(round(3.6666666666,7)) #Always returns a float
print(True and False)
print(True or False)
print(not True)
print(3==4) #comparisons. Returns True or False
print(3!=4) #not equal. Returns True or False
print('*'*80)
#ASCII and numerical basis
print(ord("a")) #returns the number in ASCII representing a string
print(chr(22))
print(hex(22)) #in you need help, in the interpreter you put help().Here you can put the mouse below a function
print(bin(22))
print('*'*80)
#Conversions between data types
print(float(1))
print(bool(1)) #only is False when "", 0.0 or 0.
print(str(1))
print(int(0.1)) #Returns the integer part
print(bool(0.0))
print(str(1.02))
print(int(True))
print(float(True))
print(str(True))
print(int("10"))
#!! print(int("3.15"))
#!! print(int(""))
print (type(2.0)) #Returns the data type
print (type("Hello"))
print('*'*80)
#Variables
a=5 #Saves a space in the memory for a, and there stores the value 5
b=a+5 #Saves a space in the memory for b, and there stores the value (1st it changes a for its value and do the operations. 2nd Stores the value)
print(a)
print(b)
a=1 #Changes the value of a in the space reserved to a
print(a)
print(b) #Doesn't changed because the value of b was store when we assigned it
print('*'*80)


#4/10
base=5 #This statement tells us that we must search in a list of variables if its defined.
#It's not, so we choose a place in the memory that we are calling base. Variable address is th evalue of the variable.
# Now, I write a 5
height=4 #Do the same thing and assign a 4 to that space
base*height #Execute the expresion: 1ºRead the base, 2º read the height, 3ºDo the operation
#The interpreter transform this state into a strip or tree??
height=2 #We substitute the value for a 2
#To do the calculation, we need to execute it again

base=5
height=base #1ºLook the value of base 2ºPlace the value on the memory address
surface=base*height #1ºRead the base, 2º read the height, 3ºDo the operation 4ºAssign the value to surface
surface #print the value stored

height=4
surface #It is still 25 because we haven't updated the sentence that we have executed
surface=base*height #Now it is 20, because we have updated it the value

final_SPEED2=1 #Name valid for a variable

x=input()
x=input("What is the value of x? ")
print(x)
x=int(input("What is the value of x? "))
print(x)

#Exceptions
"123".isdigit()
"popo".isdigit()
#!!"-123".isdigit()
"-123".lstrip("-").isdigit() #In case we have this character(), we eliminate it