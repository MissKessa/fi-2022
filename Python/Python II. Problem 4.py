#Python II. Problem 4
import random
random_number= random.randint(0,9)
guess= int(input("Guess the number. Write your guess:"))

print("Did you guess my number?",random_number)
print("Your guess is:",(random_number==guess))