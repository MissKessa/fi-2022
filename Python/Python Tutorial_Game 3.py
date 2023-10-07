#Python Tutorial_Game 3
import random
runs=10
counter_wins=0
counter_loses=0
print("0-Rock, 1-Paper, 2-Scissors")
for i in range(0,runs,1):
    while True:
        while True:
            a=input("Write your option: ")
            if a.lstrip("-").isdigit():
                break
        a=int(a)
        if a>=0 and a<=2:
            break
    b=random.randint(0,2)

    if a==b:
        print("Tie")
        
    if (a==2 and b==0) or (a==1 and b==2) or (a==0 and b==1):
        print("You lose this round")
        counter_wins+=1
    if (a==0 and b==2) or (a==2 and b==1) or (a==1 and b==0):
        print("You win this round")
        counter_loses+=1

if counter_loses==counter_wins:
    G3_Result="Tie"
elif counter_loses>counter_wins:
    G3_Result="Lose"
else:
    G3_Result="Win"