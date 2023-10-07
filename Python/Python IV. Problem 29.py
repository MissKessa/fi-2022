#Python IV. Problem 29
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break
for i in range (n,0,-1):
    for j in range (1,i+1,1):
        print(j,end=" ")
    print()