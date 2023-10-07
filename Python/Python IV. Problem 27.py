#Python IV. Problem 27
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break
while True:
    while True:
        m=input("Write another number: ")
        if m.lstrip("-").isdigit():
            break 
    m=int(m)
    if m>0:
        break

for i in range (1,n+1,1):
    for j in range (1,m+1,1):
        print(i,j, sep="",end=" ")
    print()