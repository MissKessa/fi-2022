#Python IV. Problem 29_while
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break

while n>0:
    j=1
    while j<=n:
        print(j, end=" "),
        j+=1
    n-=1
    print()