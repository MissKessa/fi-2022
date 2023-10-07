#Python 3. Problem 12
import math
a=float(input("Write the first coefficient: "))
b=float(input("Write the second coefficient: "))
c=float(input("Write the third coefficient: "))

if (b**2)-4*a*c==0:
    root=(-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
    print("It has a double root")
    print("The root is:", root)
elif (b**2)-4*a*c>0:
    root_1=(-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
    root_2=(-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
    print("It has 2 different roots")
    print("The first root is:", root_1)
    print("The second root is:", root_2)
else:
    print("It has imaginary roots")