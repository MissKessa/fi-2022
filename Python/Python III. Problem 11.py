#Python 3. Problem 11
year=int(input("Write a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is a leap year")
else:
    print(year, "isn't a leap year")