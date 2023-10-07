#Python 3. Problem 7
income=float(input("What is your annual income? "))

if income<12000:
    print("You don't need to pay")
elif income<35000:
    print("The ratio you pay is 20%")
    print("You need to pay:",round(income*0.20),2)
    print("The montly payment is:",round(income/12,2))
elif income<50000:
    print("The ratio you pay is 30%")
    print("You need to pay:",round(income*0.30,2))
    print("The montly payment is:",round(income/12,2))
elif income<70000:
    print("The ratio you pay is 35%")
    print("You need to pay:",round(income*0.35,2))
    print("The montly payment is:",round(income/12,2))
else:
    print("The ratio you pay is 50%")
    print("You need to pay:",round(income*0.50,2))
    print("The montly payment is:",round(income/12,2))