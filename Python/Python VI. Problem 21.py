#Python VI. Problem 21
def create_multiplication(number):
    tables=[]
    for i in range (1,number+1,1):
        row=[]
        for j in range (1,number+1,1):
            row.append(i*j)
        tables.append(row)
    return tables

def print_tables(number):
    tables=create_multiplication(number)
    for i in range(1,number+1,1):
        if i==1:
            print("\t", end="")
        print("*",i,end="  ")
    print()
    for i in range(1,number+1,1):
        print("Table",i,":",end=" ")
        for j in range (0,number,1):
            print(tables[i-1][j],end="   ")
        print()

print_tables(10)