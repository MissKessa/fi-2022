#Python I. Problem 5
t1_F=float(input("Write a temperature in ºF: "))
t2_C=(t1_F-32)*5/9
t3_F= (t2_C*9/5)+32
t1_F=str(t1_F)
t2_C=str(t2_C)
t3_F=str(t3_F)
print(t1_F+"ºF")
print(t2_C+"ºC")
print(t3_F+"ºF")