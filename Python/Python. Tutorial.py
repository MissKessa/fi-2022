#Python Tutorial
import random
while True:
    runs=10
    counter_wins_or_ties=0

    for i in range (0,runs):
        while True:
            while True:
                guess=input("Write a number between 0 and 1: ")
                if guess.lstrip("-").isdigit():
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
    if G1_Result:
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
        if G2_Result:
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


            if G3_Result=="Win" or G3_Result=="Lose" :
                print(f"You {G3_Result}")
                break
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        if ((dice1%2==0 and dice2%2==0) or (dice1+dice2)%2==0):
            print("You get out of the dungeons")
            G4_Result=True
        else:
            G4_Result=False
        if not G4_Result:
            print("You lose")
            break
    else:
        print("You lose")