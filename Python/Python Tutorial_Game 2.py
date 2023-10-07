#Python Tutorial_Game 2
import random

counter_wins=0
counter_loses=0
while counter_loses!=3 and counter_wins!=3:
    while True:
        guess=input("Write a letter: ")
        if len(guess)==1 and guess.isalpha():
            break 
    guess=guess.lower()
    guess=ord(guess)

    random_number_1=random.randint(ord("a"),ord("z"))
    random_number_2=random.randint(ord("a"),ord("z"))
    if (guess>=random_number_1 and guess<=random_number_2) or (guess>=random_number_2 and guess<=random_number_1):
        print("You win this round")
        counter_wins+=1
        counter_loses=0
    else:
        print("You lose this round")
        counter_loses+=1
        counter_wins=0

if counter_wins==3:
    G2_Result=True
else:
    G2_Result=False