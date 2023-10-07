#Python IV. Problem 18
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>=0:
        break
n=int(n)
for i in range (2,n+1,1): #all the numbers are divisible by 1, so I escape it
    if n%i==0:
        print("The number is divisible by",i)
