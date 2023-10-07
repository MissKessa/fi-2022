#Python IV_Additional. Problem 5
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

#if copies>100:
    #total_price*=(1-0.10)

#elif copies>= 500 and copies<=1000:
    #total_price*=(1-0.10)
    #total_price*=(1-0.002)*(copies%100)

#if copies> 1000:
    #total_price*=(1-0.10)
    #total_price*=(1-0.002)*(copies%100)
    #total_price*=(1-0.003)*(copies%1000)


while True:
    if copies>100:
        total_price*=(1-0.10)
    if copies>= 500:
        total_price*=(1-0.002)*(copies%100)
    if copies> 1000:
        total_price*=(1-0.003)*(copies%1000)
    break

print("The price for",copies,"copies:",total_price)