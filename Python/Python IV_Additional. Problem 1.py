#Python IV_Additional. Problem 1
max_number=0
min_number=0
position_max=0
position_min=0
for i in range (1,10+1,1):
    while True:
        number=input("Write number: ")
        if number.lstrip("-").isdigit():
            break
    number=int(number)
    if i==1 or number>max_number:
        max_number=number
        position_max=i
    if i==1 or number<min_number:
        min_number=number
        position_min=i

print("The highest number is",max_number,"and its position is", position_max)
print("The lowest number is",min_number,"and its position is", position_min)