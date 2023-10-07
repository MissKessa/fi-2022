#Python IV. Problem 23
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break


for i in range (0,n,1):
    for j in range (0,n,1):
        print("*",end="")
    print()