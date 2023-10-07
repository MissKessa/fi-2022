################################################################################
# Exceptions
###
 
try:
    5/0
    print("No exception")
except ZeroDivisionError as e:
    print("Catched exception:", e)
finally:
    print("Finally")
 
 
 
def ask_int_old(message):
    while True:
        value = input(message)
        if value.lstrip("-").isdigit():
            return int(value)
        print("That was not an integer. Try again.")
 
def ask_int_new(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("That was not an integer. Try again.")
 
################################################################################
# Comprehension lists
###
 
numbers = list(range(10))
squares1 = []
for number in numbers:
    squares1.append(number**2)
 
squares2 = [number**2 for number in numbers]
 
print(squares1 == squares2)
 
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number**2)
 
even_squares = [number**2 for number in numbers if number % 2 == 0]
 
################################################################################
# Nested comprehension lists
###
l = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_l = []
 
for sublist in l:
    for val in sublist:
        flatten_l.append(val)
 
flatten_l = [val for sublist in l for val in sublist]
 
print(flatten_l)
 
################################################################################
# Tuplas
###
 
def divmod(a, b):
    return a // b, a % b
 
quotient, remainder = divmod(5, 2)
t = divmod(5, 2)
print(quotient == t[0])
print(remainder == t[1])
t[0] = 100
 
################################################################################
# Dictionaries
###
 
l = ["pepe", 89, "male"]
d = {"name": "pepe", "age": 89, "gender": "male"}
print(l[0] == d["name"])
print(l[1] == d["age"])
print(l[2] == d["gender"])
 
# try:
#     print(l[100])
# except IndexError as e:
#     print("Not found:", e)
 
# try:
#     print(d["surname"])
# except KeyError as e:
#     print("Not found:", e)
 
print(d)
d["name"] = "juan"
d["surname"] = "perez"
del d["age"]
print(d)
 
################################################################################
# Comprehension dictionaries
###
 
d = {c: ord(c) for c in "aBcDe"}
print(d)
 
d = {c: ord(c) for c in "aBcDe" if c.isupper()}
print(d)