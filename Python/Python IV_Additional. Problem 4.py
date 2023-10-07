#Python IV_Additional. Problem 4
while True:
    while True:
        price=input("Write the price per copie: ")
        if price.lstrip("-").isdigit():
            break
    price=float(price)
    if price>0 and price<=1:
        break
while True:
    copies=input("How many copies do you want to do? ")
    if copies.lstrip("-").isdigit():
        break
copies=int(copies)

total_price=copies*price
if copies>=100 and copies<=200:
    total_price*=(1-0.12)
elif copies> 200 and copies<=400:
    total_price*=(1-0.15)
elif copies> 400:
    total_price*=(1-0.18)
print("The price for",copies,"copies:",total_price)