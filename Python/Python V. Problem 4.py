#Python V. Problem 4
def is_a_leap_year(year):
    """Returns if a year is leap or not. A leap year must be either divisible by 4
but not by 100 or divisible by 400."""
    return (year%4==0 and year%100!=0) or year%400==0


for i in range (1,2022+1,1):
    result=is_a_leap_year(i)
    if result:
        print(i,"is a leap year")
    else:
        print(i,"isn't a leap year")