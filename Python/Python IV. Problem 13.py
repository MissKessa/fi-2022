#Python IV. Problem 13
sum_even=0
sum_odd=0
counter_even=0
counter_odd=0
while True:
    while True:
        number=input("Write a number: ")
        if number.lstrip("-").isdigit():
            break  
    number=int(number)
    if number<0:
        break
    if number%2==0:
        counter_even+=1
        sum_even+=number
    if number%2!=0:
        counter_odd+=1
        sum_odd+=number

average_even=sum_even/counter_even
average_odd=sum_odd/counter_odd
print("The average of the even numbers is", average_even)
print("The average of the odd numbers is", average_odd)