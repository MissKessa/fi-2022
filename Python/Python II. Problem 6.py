#Python II. Problem 6
name= input("Write the name of the student:")
mark_1= float(input("Write the first mark of the student:"))
mark_2= float(input("Write the second mark of the student:"))

average=round((mark_1+mark_2)/2,2)
print("The average mark of",name,"is",average)
print("Pass the subject:", average>=5)