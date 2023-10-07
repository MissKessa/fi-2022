#Python Tutorial_Game 4
#To get out of the dungeons: throw two dice, if the numbers are even or the sum is even
#then you get out of the dungeons. Otherwise, you lose.
import random
dice1=random.randint(1,6)
dice2=random.randint(1,6)
if ((dice1%2==0 and dice2%2==0) or (dice1+dice2)%2==0):
    print("You get out of the dungeons")
    G4_Result=True
else:
    G4_Result=False