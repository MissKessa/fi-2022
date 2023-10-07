#Python IV. Problem 3
while True:
    while True:
        end=input("Write an number greater than 0: ")
        if end.lstrip("-").isdigit():
            break
    end=int(end)
    if end>0:
        break
product=1

while end>1:
    product*=end
    end-=1
print("The product of the integer numbers between 1 and the number is:",product)