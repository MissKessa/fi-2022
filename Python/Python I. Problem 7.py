#Python I. Problem 7
name_1= input("What's the name of the first friend?: ")
height_1=float(input("What's the height of "+name_1+" ?: "))
name_2= input("What's the name of the second friend?:")
height_2=float(input("What's the height of "+name_2+" ?: "))
name_3= input("What's the name of the third friend?: ")
height_3=float(input("What's the height of "+name_3+" ?: "))

max=max(height_1,height_2,height_3)
min=min(height_1,height_2,height_3)
print("Is "+name_1+" the tallest? "+ str(max==height_1))
print("Is "+name_2+" the tallest? "+ str(max==height_2))
print("Is "+name_3+" the tallest? "+ str(max==height_3))
print("Is "+name_1+" the smallest? "+ str(min==height_1))
print("Is "+name_2+" the smallest? "+ str(min==height_2))
print("Is "+name_3+" the smallest? "+ str(min==height_3))