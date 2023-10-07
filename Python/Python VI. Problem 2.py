#Python VI. Problem 2
list1=[5,8,10]
list2=[3,2,9,12,4]

print(list1[0]+list2[0])

print(list1[-1]+list2[-1])

for i in range (len(list1)):
    if list1[i]==8:
        list1[i]=0
#or list1[1]=0
print(list1)