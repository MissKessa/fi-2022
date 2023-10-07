#Python IV. Problem 9_while
while True:
    while True:
        lower_limit=input("Write a lower limit greater than 0: ")
        if lower_limit.lstrip("-").isdigit():
            break
    lower_limit=int(lower_limit)
    if lower_limit>0:
        break

while True:
    while True:
        upper_limit=input("Write a upper limit greater than 0 and greater than the lower limit: ")
        if upper_limit.lstrip("-").isdigit():
            break
    upper_limit=int(upper_limit)
    if (upper_limit>0) and (upper_limit>=lower_limit):
        break

summation=0

while lower_limit<=upper_limit:
    summation+=(lower_limit**2)+(1/lower_limit)
    lower_limit+=1
print("The summation is: ", summation)
