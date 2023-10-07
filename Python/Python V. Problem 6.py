#Python V. Problem 6
import utils

def calculate_BMI(weight,height):
    """This functions returns the value of the BMI"""
    return weight/(height**2)


weight=round(utils.read_positive_float("Write your weight: "),2)
height=round(utils.read_positive_float("Write your height: "),2)
BMI=calculate_BMI(weight,height)
if BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")
