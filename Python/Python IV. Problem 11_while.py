#Python IV. Problem 11_while
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break
    n=int(n)
    break

while True:
    while True:
        m=input("Write a number greater than the first one: ")
        if m.lstrip("-").isdigit():
            break
    m=int(m)
    if (m>=n):
        break

while n<=m:
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
    n+=1