#Python 3. Problem 14
print("0-Rock, 1-Paper, 2-Scissors")
a=int(input("User 1 write your option: "))
b=int(input("User 2 write your option: "))

if a==b:
    print("Tie")
if a==0 and b==1:
    print("User 2 wins")
if a==0 and b==2:
    print("User 1 wins")

if a==1 and b==0:
    print("User 1 wins")
if a==1 and b==2:
    print("User 2 wins")

if a==2 and b==0:
    print("Tie")
if a==2 and b==1:
    print("User 1 wins")