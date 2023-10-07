#Python Tutorial_Game 1
import random

runs=10
counter_wins_or_ties=0

for i in range (0,runs):
    while True:
        while True:
            guess=input("Write a number between 0 and 1: ")
            counter_dot=0
            digit=0
            correct_number=True
            for i in range (0,len(guess),1):
                if i==".":
                    counter_dot+=1
                if counter_dot>1 or guess[i:i]:
                   correct_number=False
            if correct_number==True:
                break
        guess=float(guess)
        if guess>=0 and guess<=1:
            break
    random_number=random.uniform(0.0,1.0)
    difference=random_number-guess
    if difference<0:
        difference*=-1
    
    if difference<0.125:
        print("You win this round")
        counter_wins_or_ties+=1
    elif difference<0.2:
        print("It's a tie")
        counter_wins_or_ties+=1
    else:
        print("You lose this round")

if counter_wins_or_ties>runs/2:
    G1_Result=True
else:
    G1_Result=False
