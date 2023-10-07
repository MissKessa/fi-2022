#Python VII. Problem 3
def calculate_p(coefficients,x):
    """Calculats the value of p(x), p is a polynomial"""
    result=0
    for i in range(0,len(coefficients),1):
        result+=int(coefficients[i])*int(x)
    return result

polynomial=input("Where did you store the polynomial? ")
values=input("Where did you store the values? ")

p=open(polynomial+".txt","r")
v=open(values+".txt","r")
all_coefficients=p.readlines()
all_values=v.readlines()
p.close()
v.close()

coefficients=all_coefficients[0].strip().split(" ")
values=all_values[0].strip().split(" ")

for i in range(0,len(values),1):
    print(values[i],"--p("+"values[i]"+")=",calculate_p(coefficients,values[i]))