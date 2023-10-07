#Python IV. Problem 16
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break
n=int(n)

inverted_n=""
while n>0:
    digit=str(n%10)
    n=n//10
    inverted_n+=digit

print("The inverted number is",inverted_n)