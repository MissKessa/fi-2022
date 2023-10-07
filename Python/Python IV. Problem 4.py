#Python IV. Problem 4
while True:
    while True:
        n=input("Write an number greater than 0: ")
        if n.lstrip(" ").isdigit():
            break
    n=int(n)
    if n>0:
        break

a="*"
print(a*n)
#or with while loops