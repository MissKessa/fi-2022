#Python IV. Problem 14
while True:
    while True:
        a=input("Write a number: ")
        if a.lstrip("-").isdigit():
            break 
    a=int(a)
    if a>=0:
        break
while True:
    while True:
        b=input("Write another number: ")
        if b.lstrip("-").isdigit():
            break 
    b=int(b)
    if b>=0:
        break 

product_a=0
for i in range (0,b,1):
    product_a+=a
print ("The product is",product_a)