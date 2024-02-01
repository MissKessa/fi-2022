import random


def throw_dice(sides, amount):
    """Throw a dice with a given amount of sides a given amount of times."""

    total = 0
    for i in range(amount):
        x = random.randint(1, sides)
        print(f"Rolled a {x} on a {sides} sided dice")
        total += x
    print(f"The sum of the {amount} dice is {total}")
    return total


def scale_monster_level(level, side):
    """Scale the monster level based on the side and the player level."""

    if side == 2:
        monster_level = level - 2
    elif side == 3:
        monster_level = level - 1
    elif side == 4:
        monster_level = level
    elif side == 5:
        monster_level = level + 1
    elif side == 6:
        monster_level = level + 2
    if monster_level < 1:
        monster_level = 1
    return monster_level


def ask_fight_choice():
    """Ask the player what they want to do in a fight."""

    while True:
        choice = input("What do you want to do: [a]ttack or [r]un? ").lower()
        if choice == "attack" or choice == "a":
            return "attack"
        elif choice == "run" or choice == "r":
            return "run"
        else:
            print("Invalid choice")


def fight(health, monster_health, level, monster_level):
    """Fight a monster."""

    phase = 0
    while True:
        phase += 1

        print()
        print(f"PHASE {phase}")
        print("You have", health, "health")
        print("The monster has", monster_health, "health")
        choice = ask_fight_choice()
        if choice == "attack":
            attack = throw_dice(6, 2) + round(health / 2)
            monster_attack = throw_dice(6, 2) + round(monster_health / 2)
            diff = attack - monster_attack
            if diff > 0:
                monster_health -= diff
                print(f"You hit the monster for {diff} damage")
            elif diff < 0:
                health += diff
                print(f"The monster hits you for {-diff} damage")
            if monster_health <= 0:
                print("You killed the monster")
                return health, level + monster_level
            if health <= 0:
                print("The monster killed you")
                return health, level
        elif choice == "run":
            if throw_dice(6, 1) > 3:
                print("You successfully ran away")
                return health, level
            print("You failed to run away")
            monster_attack = throw_dice(6, 2)
            health -= monster_attack
            print(f"The monster hits you in the back for {monster_attack} damage")
            if health <= 0:
                print("The monster killed you")
                return health, level


def play():
    """ Main game loop."""

    turn = 0
    health = 100
    level = 1
    while True:
        turn += 1

        print()
        print("*" * 80)
        print(f"* Turn {turn}")
        print("*" * 3)
        print()

        print("Your health is", health)
        print("Your level is", level)
        side = throw_dice(6, 1)
        if side == 1:
            print("You find a health potion")
            health += 20
        else:
            monster_level = scale_monster_level(level, side)
            print("You find a monster of level", monster_level)
            monster_health = 10 * monster_level
            health, level = fight(health, monster_health, level, monster_level)
            if health <= 0:
                return level


print("Welcome to the")
# From: https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=Dungeon%20of%20Doom!!!
print("""
▓█████▄ █    ██ ███▄    █  ▄████▓█████ ▒█████  ███▄    █     ▒█████   █████▒   ▓█████▄ ▒█████  ▒█████  ███▄ ▄███▓ ▐██▌  ▐██▌  ▐██▌ 
▒██▀ ██▌██  ▓██▒██ ▀█   █ ██▒ ▀█▓█   ▀▒██▒  ██▒██ ▀█   █    ▒██▒  ██▓██   ▒    ▒██▀ ██▒██▒  ██▒██▒  ██▓██▒▀█▀ ██▒ ▐██▌  ▐██▌  ▐██▌ 
░██   █▓██  ▒██▓██  ▀█ ██▒██░▄▄▄▒███  ▒██░  ██▓██  ▀█ ██▒   ▒██░  ██▒████ ░    ░██   █▒██░  ██▒██░  ██▓██    ▓██░ ▐██▌  ▐██▌  ▐██▌ 
░▓█▄   ▓▓█  ░██▓██▒  ▐▌██░▓█  ██▒▓█  ▄▒██   ██▓██▒  ▐▌██▒   ▒██   ██░▓█▒  ░    ░▓█▄   ▒██   ██▒██   ██▒██    ▒██  ▓██▒  ▓██▒  ▓██▒ 
░▒████▓▒▒█████▓▒██░   ▓██░▒▓███▀░▒████░ ████▓▒▒██░   ▓██░   ░ ████▓▒░▒█░       ░▒████▓░ ████▓▒░ ████▓▒▒██▒   ░██▒ ▒▄▄   ▒▄▄   ▒▄▄  
 ▒▒▓  ▒░▒▓▒ ▒ ▒░ ▒░   ▒ ▒ ░▒   ▒░░ ▒░ ░ ▒░▒░▒░░ ▒░   ▒ ▒    ░ ▒░▒░▒░ ▒ ░        ▒▒▓  ▒░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░   ░  ░ ░▀▀▒  ░▀▀▒  ░▀▀▒ 
 ░ ▒  ▒░░▒░ ░ ░░ ░░   ░ ▒░ ░   ░ ░ ░  ░ ░ ▒ ▒░░ ░░   ░ ▒░     ░ ▒ ▒░ ░          ░ ▒  ▒  ░ ▒ ▒░  ░ ▒ ▒░░  ░      ░ ░  ░  ░  ░  ░  ░ 
 ░ ░  ░ ░░░ ░ ░   ░   ░ ░░ ░   ░   ░  ░ ░ ░ ▒    ░   ░ ░    ░ ░ ░ ▒  ░ ░        ░ ░  ░░ ░ ░ ▒ ░ ░ ░ ▒ ░      ░       ░     ░     ░ 
   ░      ░             ░      ░   ░  ░   ░ ░          ░        ░ ░               ░       ░ ░     ░ ░        ░    ░     ░     ░    
 ░                                                                              ░                                                  
""")
level = play()
print()
print("The only to scape is to")
# From: https://patorjk.com/software/taag/#p=testall&f=Graffiti&t=Die!!!
print("""
▓█████▄ ██▓█████  ▐██▌  ▐██▌  ▐██▌ 
▒██▀ ██▓██▓█   ▀  ▐██▌  ▐██▌  ▐██▌ 
░██   █▒██▒███    ▐██▌  ▐██▌  ▐██▌ 
░▓█▄   ░██▒▓█  ▄  ▓██▒  ▓██▒  ▓██▒ 
░▒████▓░██░▒████▒ ▒▄▄   ▒▄▄   ▒▄▄  
 ▒▒▓  ▒░▓ ░░ ▒░ ░ ░▀▀▒  ░▀▀▒  ░▀▀▒ 
 ░ ▒  ▒ ▒ ░░ ░  ░ ░  ░  ░  ░  ░  ░ 
 ░ ░  ░ ▒ ░  ░       ░     ░     ░ 
   ░    ░    ░  ░ ░     ░     ░    
 ░                                 
""")
print("You reached level", level)