#Python IV. Problem 15
while True:
    while True:
        a=input("Write a number: ")
        if a.lstrip("-").isdigit():
            break 
    a=int(a)
    if a>=0:
        break
while True:
    while True:
        b=input("Write another number: ")
        if b.lstrip("-").isdigit():
            break 
    b=int(b)
    if b>=0:
        break

quotient=0
remainder=0
while a>=b:
    remainder=a-b
    a=remainder
    quotient+=1 #quotient is the counter of times we substract
if a<b:
    remainder=a
print ("The quotient is",quotient)
print ("The remainder is",remainder)