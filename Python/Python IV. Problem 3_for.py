#Python IV. Problem 3_for
while True:
    while True:
        end=input("Write an number greater than 0: ")
        if end.lstrip("-").isdigit():
            break
    end=int(end)
    if end>0:
        break
product=1

for i in range(2,end,1):
    product*=i
print("The product of the integer numbers between 1 and the number is:",product)