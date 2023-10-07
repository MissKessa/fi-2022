#Python 4. Problem 2
end=-1
while end<0:
    end=input("Write an number greater than 0: ")
    while not end.lstrip("-").isdigit():
        end=input("Write an number greater than 0: ")
    end=int(end)

sum_integers=0

for i in range(1,end,1):
    sum_integers+=i
print("The sum of the integer numbers between 1 and",end,"is:",sum_integers)