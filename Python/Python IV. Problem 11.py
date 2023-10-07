#Python IV. Problem 11
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

for i in range(n,m+1,1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")