#Python IV. Problem 21
while True:
    while True:
        n=input("Up to what Fibonnacci term you want to calculate?: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>=1:
        break
n=int(n)
a=0
b=1

if n>=1:
    print(a)
if n>=2:
    print(b)
if n>=3:
    for i in range (3,n+1):
        c=a+b
        a=b
        b=c
        print(c)