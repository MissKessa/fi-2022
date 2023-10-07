#Python IV. Problem 19
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>0:
        break
n=int(n)

sum_divisors=0
for i in range (1,n,1):
    if n%i==0:
        sum_divisors+=i
if sum_divisors==n:
    print (n,"is a perfect number") 
else:
    print (n,"is not a perfect number") 

#or:
#print ("Is n a perfect number?",sum_divisor==n)