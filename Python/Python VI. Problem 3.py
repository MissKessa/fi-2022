#Python VI. Problem 3
list1=[5,8,10]
list2=[3,2,9,12,4]
list3=list1+list2

list3=list2 #reference
print(list3)

list3[0]=7
print(list3)

print(list2)