#Python VII. Problem 2
def ask_values(message):
    """Asks the user to write something.
The user must answer 'No' to stop introducing coefficients"""
    values=[]
    while True:
        value=input(message)
        if value.strip().lstrip("-").isdigit():
            values.append(int(value))
        elif value.strip().lower()=="no":
            return values


name_file=input("Write the name of your file: ")
L=ask_values("Write the values of x: ")

f=open(name_file+".txt","a")
for i in range(0,len(L),1):
    f.write(str(L[i])+" ")
f.close()