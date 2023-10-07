#Python IV_Additional. Problem 3
sum_even=0
counter_even=0
sum_odd=0
counter_odd=0

for i in range (1,200+1,1):
    if i%2==0:
        sum_even+=i
        counter_even+=1
    else:
        sum_odd+=i
        counter_odd+=1

average_even=sum_even/counter_even
average_odd=sum_odd/counter_odd
print("The average of even numbers is",average_even)
print("The average of odd numbers is",average_odd)