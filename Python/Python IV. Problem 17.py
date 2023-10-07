#Python IV. Problem 17
while True:
    while True:
        n=input("Write a number: ")
        if n.lstrip("-").isdigit():
            break 
    n=int(n)
    if n>=0:
        break
n=int(n)

counter_figures=0
if n==0:
    counter_figures=1
while n>0: #if n>=0 it creates an infite loop
    n=n//10
    counter_figures+=1
print("The number of figures is",counter_figures)