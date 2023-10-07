#Python IV. Problem 12
sum_number=0
counter=0
while True:
    while True:
        number=input("Write a number: ")
        if number.lstrip("-").isdigit():
            break  
    number=int(number)
    if number<0:
        break
    counter+=1
    sum_number+=number

average=sum_number/counter
print("The average is", average)