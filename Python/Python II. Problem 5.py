#Python II. Problem 5
weight= float(input("Write your weight:"))
height= float(input("Write your height:"))

body_max_index=weight/(height**2)

print("[0, 18.5)?", body_max_index>=0 and body_max_index<18.5)
print("[18.5, 25)?", body_max_index>=18.5 and body_max_index<25)
print("[25, 30)?", body_max_index>=25 and body_max_index<30)
print("[30, 50)?", body_max_index>=30 and body_max_index<50)