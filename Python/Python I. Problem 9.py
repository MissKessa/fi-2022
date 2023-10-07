#Python I. Problem 9
year=int(input("Write a year: "))

print("Is "+str(year)+" a leap year? " + (str((year%4==0)or (year%400==0))))