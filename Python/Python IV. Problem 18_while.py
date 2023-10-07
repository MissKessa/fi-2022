#Python IV. Problem 18_while
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>=0:
        break
n=int(n)
divisor=2
while divisor<=n:
    if n%divisor==0:   
        print("The number is divisible by",divisor)
    divisor+=1