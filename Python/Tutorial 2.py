#Handle exceptions
try:
    x=5/0
    print(x) #not going to be printed

except ZeroDivisionError as e:  #catching error in e
    print("Catched exception: ", e) #to print this

finally: #always will be executed if there is one exception or not
    print("This is going to be executed no matter what")
    #very important especially with files because there if an exception appears while reading a file, 
    # the f.close() will not be executed. SO we have a problem, but if i put it on finally always close

try:
    x=5/1
    print(x) # printed

except ZeroDivisionError as e:  #catching error in e
    print("Catched exception: ", e) #to print this

finally: #always will be executed if there is one exception or not
    print("This is going to be executed no matter what")



def ask_int_old(message):
    while True:
        value=inpu(message)
        if value.strip("-").isdigit():
            return int(value)
        print("That's not an integer.Try again")

def ask_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("That's not an integer.Try again")


#comprehension list####################################
numbers=list(range(10))
#from this:
squares=[]
for number in numbers:
    squares.append(number**2)
#to this:
squares=[number**2 for number in numbers]

#with ifs
even_squares=[]
for number in numbers:
    if number%2==0:
        even_squares.append(number**2)

even_squares=[number**2 for number in numbers if number%2==0]

#with nested loops
#Nested comprehension list####################################
l=[[1,2,3],[4,5]]
flatten_l=[]

for sublist in l: #1st loop
    for val in sublist: #2nd loop
        flatten_l.append(val)

flatten_l=[val for sublist in l for val in sublist] #append   1st loop    2nd loop
#you can also put ifs inside

#Tuples####################################

def divmod(a,b):
    return a//b,a%b #you are not returning 2 thing, you are retuning a tupla

quotient,remainder=divmod(5,2)
t=divmod(5,2) #with one variable i am using a tupla, that is one special list- Inmutable lists (you cannot modying as list)
print(quotient==t[0])
print(remainder==t[1])

#an eroor appears with: t[0]=100 because it's inmatuble

#to create a tuple:
t=(0,1) #but is not mandatory the (), but yes ,
t=0,1 #so in the return you are creating a tuple


#Dictionaries####################################
l=["pepe",89,"male"]  #instead of this
#a dictionary:
d={"name":"pepe","age":89,"gender":"male"}
print(l[0]==d["name"])
print(l[1]==d["age"])
print(l[2]==d["gender"])

try:
    print(l[100])
except IndexError as e:
    print("Not found: ",e)

try:
    print(d["surname"])
except KeyError as e:
    print("Not found: ",e)

print(d)
d["name"]="Juan" #modying the dictionary
print(d)
#to append something: I use a new key, an assign a value
d["surname"]="Pérez"
print(d)

#for removing:
del d["age"]
print(d)
#Comprehension dictionaries####################################
d={c: ord(c) for c in "aBcDe"} #like list but with {}, and we need key:value
#we are creating a dictioanary with a character and its value

d={c: ord(c) for c in "aBcDe" if c.isupper()}