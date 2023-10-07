#Python IV. Problem 26_while
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break

i=1 #counter of the row 
while i<=n:
    j=1 #counter of the column
    while j<=n:
        print(i,j, sep="", end=" "),
        j+=1
    i+=1
    print()