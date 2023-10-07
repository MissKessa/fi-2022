#Python 3. Problem 15
import random
print("0-Rock, 1-Paper, 2-Scissors")
a=int(input("User 1 write your option: "))
b=random.randint(0,2)

if a==b:
    print("Tie")
if a==0 and b==1:
    print("The computer wins")
if a==0 and b==2:
    print("User 1 wins")

if a==1 and b==0:
    print("User 1 wins")
if a==1 and b==2:
    print("The computer wins")

if a==2 and b==0:
    print("Tie")
if a==2 and b==1:
    print("User 1 wins")