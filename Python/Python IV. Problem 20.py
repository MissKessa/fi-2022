#Python IV. Problem 20
sum_cubed_digits=0
for i in range (100,1000,1):
    n=i
    while n>0:
        digit=n%10
        sum_cubed_digits+=digit**3
        n=n//10
    if sum_cubed_digits==i:
        print(i)


