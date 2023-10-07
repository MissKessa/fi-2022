import random
while True:
    while True:
        health=input("How many health point does your hero have? ")
        if health.lstrip("-").isdigit():
            break
    health=int(health)
    if health>=10 and health<=20:
        break
print("Welcome to the dungeon!")
turn=1
experience=1

while experience<10 and health>0:
    print("\nTURN",turn,"\nYou have",health,"health points and",experience,"experience points")
    what_appears=random.randint(0,3)#monster or drink

    if what_appears==0: #drink appears
        print("You found a mysterious potion!")
        drink=input("Do you want to drink it? ")

        if drink.lower()=="yes": #you drink it
            type_of_drink=random.randint(0,2)
            if type_of_drink==0: #poison
                print("Oh noo it is a poison!")
                health-=5
            else: #healing poison
                print("Yeah! You find a healing poison")
                health+=5

    else: #monster appears
        level_monster=random.randint(1,3)
        health_monster=level_monster
        print("A monster with level",level_monster,"appears!")
        while health_monster>0 and health>0:
            print("\nThe monster has",health_monster,"health points")
            print("You have",health,"health points and",experience,"experience points")
            fight=input("Do you want to fight? ")

            if fight.lower()=="no": #no fight
                escape=random.randint(0,1)
                if escape==0: #escape sucessfully
                    print("You run away!")
                else:
                    print("The monster hits you while escaping") #escape but hit
                    health-=level_monster
                break

            else: #fight
                attack=random.randint(0,1)
                if attack==0: #you attack
                    health_monster-=experience
                    print("You hit the monster")
                else: #monster attack
                    health-=level_monster
                    print("The monster hits you")
        if health_monster<=0:
            experience+=level_monster
            print("You defeated the monster")
    turn+=1

if experience>=10:
    print("\nYOU WIN!")
else:
    print("\nYOU LOSE")