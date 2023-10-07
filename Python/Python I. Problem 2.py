#Python I.Problem 2
a=5; b=a+5
print(a)
print(b) #a)The value is 5+5=10
a=7
print(a)
print(b) #b)The value already stored because b hasn't been updated
#c) 
print(type(a)); print(type(b)) #Integers
#d)
a=5.0; b=a+5
print(type(a)); print(type(b)) #Floats
#e)
print(b)
b=b+1 #Adds 1 to the value stored in b, and the final result is stored in b
print(b)
#f)
a="Hello";b="World"
print(type(a)); print(type(b)) #Strings
print(a+b) #The strings are concatened