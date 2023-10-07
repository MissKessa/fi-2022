#Python I. Problem 10
a=float(input("Write a number: "))
b=float(input("Write a number: "))

print("Is a between 5 and 30 and b even? "+str(a>=5 and a<=30 and b%2==0))
print("Is a not between 5 and 30 or b odd? "+str((not(a>=5 and a<=30)) or b%2!=0))