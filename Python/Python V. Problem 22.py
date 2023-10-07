#Python V. Problem 22
import utils

def hotel_cost(nights):
    """Calculates the cost of the hotel"""
    return nights*140


def plane_ride_cost(city):
    """ The function should return a different price depending on the location. Below are
the valid destinations and their corresponding round-trip prices.
"Tokio": 183
"New York": 220
"London": 222
"Cabañaquinta": 475"""
    if city=="Tokio":
        return 183
    elif city=="New York":
        return 220
    elif city=="London":
        return 222
    return 475


def rental_car_cost(days):
    """Calculate the cost of renting the car: Every day you rent the car costs $40. If you rent the car
for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3
or more days, you get $20 off your total. You cannot get both of the above discounts."""
    cost=40*days
    if days>=3 and days<7:
        return cost*0.2
    elif days>=7:
        return cost*0.5
    return cost


def  trip_cost(city, days,spending_money):
    """ calculates the sum of all the costs"""
    return rental_car_cost(days)+plane_ride_cost(city)+spending_money+hotel_cost(days)


def read_city(message):
    while True:
        city=input(message)
        if city=="Tokio" or city=="New York" or city=="London" or city=="Cabañaquinta":
            return city
        print("Incorrect destination")

days=utils.read_positive_integer("Write the days you stay: ")
spending_money=utils.read_positive_integer("Write the money you are going to spend: ")
city=read_city("Write the destination: ")

costs=trip_cost(city, days,spending_money)
print("The cost of the trip",costs)