#Python IV_Additional. Problem 2
for i in range (1,1000+1,1):
    print(i)
    if i%20==0:
        continue_series=input("Do you want o continue? ")
        if continue_series.lower()=="no":
            break