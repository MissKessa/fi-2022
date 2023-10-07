#Python II. Problem 3
import math

a= float(input("Write the first coefficient of the quadratic equation as a real number: "))
b= float(input("Write the second coefficient of the quadratic equation as a real number: "))
c= float(input("Write the third coefficient of the quadratic equation as a real number: "))

root=math.sqrt((b**2)-4*a*c)
solution_1= ((-b + root)/(2*a))
solution_2= ((-b - root)/(2*a))
print("The solutions of the quadratic equation are:",solution_1,"and",solution_2)

#math domain error: the root is negative