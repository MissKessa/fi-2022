import random
# Maps ###########################################################
def print_full_map():
    """Prints the map of the mansion with a legend"""
    print("""
*******************************************************************
*   ++++++++++++++++++++++++                                      *
*   +                      +                                      *
*   +      POOL            +                                      *
*   +                      +           GARDEN                     *
*   ++++++++++++++++++++++++                                      *
*                                                                 *
*     _________________''''''_______________                      *
*     |          |                 |        |                     *
*     |  C       |       D         |   E    |                     *
*     |________  |__   ____________|        |                     *
*     |      |                     |        |        GARDEN       *
*     |  B       ___   _______   ___________|                     *
*     |______|   |      |              |    |                     *
*     |      |       F  |    G         | H  |                     *
*     |  A       |      |                   |                     *
*     |______|   |______|______________|____|                     *
*            /   /                                                *
*            /   /                                                *
*            /   /                                                *
*            /   /                                                *
*            /   /                                                *
*            /   /                                                *
*************    **************************************************

LEGEND OF THE HOUSE MAP:
'''' -> gate to the garden
// -> stone path leading to the house
++ -> pool limits
** -> property limits

ROOMS:
A: Office
B: Library
C: Casino
D: Living Room
E: Son's Bedroom
F: Kitchen
G: Master Bedroom
H: Master Bathroom
""")


###
list_rooms=["Outside","Office","Library","Casino", "Living Room","Son's Bedroom","Kitchen","Master Bedroom","Master Bathroom"]
def create_key():
    """Creates a random code for a room that will be used to unlock it
    -Returns the code for the room"""

    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    key=""
    key+=letters[random.randint(0,len(letters)-1)] #letter
    for i in range(0,3,1): #adding the numbers to the key
        key+=numbers[random.randint(0,len(numbers)-1)]
    return key


rooms={}
def assign_keys(list_rooms):
    """Assigns a key to each room (using a dictionary)
    -list_rooms: It's the list of the rooms
    -Returns a the dictionary with each room and its key"""

    for i in range (0,len(list_rooms)-1,1):
        rooms[list_rooms[i]]=create_key()
    return rooms


def ask_code(room,rooms):
    """Aks the user for the code of an specific room
    -room: It's the name of the room and we ask for the code
    -rooms: The dictionary with each room and its key"""

    i=0
    while i<10: #some prints to hide the text before this
        print()
        i+=1
    print("\nI go to the padlock of the next room. Oh no I didn't look at it very much, I remember it?")
    tries=0
    while tries<4:
        tries+=1
        guess=input("What's the code for the room? ")
        if rooms[room]==guess.strip():
            print("I did it!")
            break
        if tries==4:
            print("Wrong... again\nThe door opened... after a long long time")
        #prints some clues for the code saying one letter/number
        if tries!=4:
            clue=random.randint(0,len(rooms[room])-1)
            print("Mmm I think one part is", rooms[room][clue:clue+1])
    print("___________\n")


# Transitions ####################################################
def print_status(energy,reputation):
    """Prints the energy and reputation of the detective
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective"""

    print(f"""_____________ \nEnergy: {energy} \nReputation: {reputation} \n_____________""")


def print_day(day):
    """Prints the date according to the day
    -day: It's the day of the story"""

    print("*"*20)
    days={0:"MONDAY 1",1:"TUESDAY 2",2:"WEDNESDAY 3",3:"THURSDAY 4",4:"FRIDAY 5",5:"SATURDAY 6",6:"SUNDAY 7",
    7:"MONDAY 8",8:"TUESDAY 9",9:"WEDNESDAY 10",10:"THURSDAY 11 - TRIAL"}

    print(days[day])
    print("*"*20)


def check_energy(energy,day):
    """Checks if the energy is 0, and a new day starts (Until it reaches day 10). The energy is restored
    -energy: It's the energy of the detective
    -day: It's the day of the story"""
    if energy<=0:
        if day<10:
            day+=1
            print_day(day)
        energy=20
    return energy,day


def print_title():
    """Prints the title of the game"""

    print("""
                ███▄ ▄███▓ █    ██  ██▀███  ▓█████▄ ▓█████  ██▀███      ███▄ ▄███▓▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ██▀███ ▓██   ██▓
                ▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒   ▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██  ██▒
                ▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒░██   █▌▒███   ▓██ ░▄█ ▒   ▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒ ▒██ ██░
                ▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄     ▒██    ▒██   ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄   ░ ▐██▓░
                ▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒░▒████▓ ░▒████▒░██▓ ▒██▒   ▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒ ░ ██▒▓░
                ░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░  ██▒▒▒ 
                ░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░   ░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░▓██ ░▒░ 
                ░      ░    ░░░ ░ ░   ░░   ░  ░ ░  ░    ░     ░░   ░    ░      ░    ▒ ▒ ░░  ░  ░  ░    ░         ░     ░░   ░ ▒ ▒ ░░  
                    ░      ░        ░        ░       ░  ░   ░               ░    ░ ░           ░              ░  ░   ░     ░ ░     
                                            ░                                     ░ ░                                       ░ ░     
    \n\n\n""")
    input("\t\t\t\t\t\t\t  Press Enter to start!\n")


def print_story():
    """Prints the beggining of the history"""

    print("""◀ A horrible murder happened last night, and there are already 4 suspects ▶

The officers are trying to keep it confidential,         Everyone has to keep calm, the police are        I know the victim, and I won't stop
but many people have a lot of doubts: This is a          trying to do the best they can.                  until I find the murderer.
really nice neighbourhood, I can not believe this        Javier P.R                                       Ana P.B
happened.
Paula D.Á
—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

These are the news that your boss puts on your desk, and he gives you your last opportunity. If you don't solve the case in 10 days until the trial, you are fired.

First things first, you have to interrogate the suspects and visit the crime scene. It won't be easy to solve the case, you will have to overcome some difficult
challenges and riddles. But be careful with your actions, as your reputation will also be on the line.\n\n\n""")


def print_tutorial():
    """Prints a tutorial to how show to play the game"""

    choice=input("Do you want to see a tutorial? (yes/no)\n").strip().lower()
    if choice=="yes":
        print("""\tFirst, the interrogation, you will be able to ask questions to the suspects.
    After, you will keep going room by room until you complete all the games (one per room). You need to have the dices on your side, which will help you observe the
clues to uncover the mystery (each zone in the room will be useful and unlock the game; or it won't give you any information).

Also be careful with your actions because each of them will consume your energy, and spending too many tries at a game will decrease your reputation.
    -Winning game, will give you a clue and the code for the next room.
    -Losing a game, will give you a wrong clue and the code for the next room

Then, when you finishig all the rooms or if the final day (10) cames you will need to expose your conclusions to the almighty judge. Counterpoints may be made by the
suspect, so be prepared to prove the truth behind your arguments! Your performance here will affect your result.
_____________________________________________________________________________________________________________________________________________________________________\n\n""")


def print_credits():
    """Prints the final credits"""

    print("""
████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗
   ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║
   ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                                                       
This game was maded by: Ana Pérez, Javier Pérez and Paula Díaz
--------------------------------------------------January 2023

Thanks for playing

Symbols and fonts from:
-https://patorjk.com/software/taag/#p=about&f=Graffiti&t=Type%20Something%20
-https://es.piliapp.com/symbol/""")


def print_rooms(number_room):
    """Prints the title for the room
    -number_room: It's the number of the room"""

    titles=[
"""
   ___        _       _     _      
  / _ \ _   _| |_ ___(_) __| | ___ 
 | | | | | | | __/ __| |/ _` |/ _ \\
 | |_| | |_| | |_\__ \ | (_| |  __/
  \___/ \__,_|\__|___/_|\__,_|\___|                                
""","""
   ___   __  __ _          
  / _ \ / _|/ _(_) ___ ___ 
 | | | | |_| |_| |/ __/ _ \\
 | |_| |  _|  _| | (_|  __/
  \___/|_| |_| |_|\___\___|
                           
""","""
  _     _ _                          
 | |   (_) |__  _ __ __ _ _ __ _   _ 
 | |   | | '_ \| '__/ _` | '__| | | |
 | |___| | |_) | | | (_| | |  | |_| |
 |_____|_|_.__/|_|  \__,_|_|   \__, |
                               |___/ 
""","""
   ____          _             
  / ___|__ _ ___(_)_ __   ___  
 | |   / _` / __| | '_ \ / _ \ 
 | |__| (_| \__ \ | | | | (_) |
  \____\__,_|___/_|_| |_|\___/ 
                               
""","""
  _     _       _               ____                       
 | |   (_)_   _(_)_ __   __ _  |  _ \ ___   ___  _ __ ___  
 | |   | \ \ / / | '_ \ / _` | | |_) / _ \ / _ \| '_ ` _ \ 
 | |___| |\ V /| | | | | (_| | |  _ < (_) | (_) | | | | | |
 |_____|_| \_/ |_|_| |_|\__, | |_| \_\___/ \___/|_| |_| |_|
                        |___/                              
""","""
  ____              _       ____           _                           
 / ___|  ___  _ __ ( )___  | __ )  ___  __| |_ __ ___   ___  _ __ ___  
 \___ \ / _ \| '_ \|// __| |  _ \ / _ \/ _` | '__/ _ \ / _ \| '_ ` _ \ 
  ___) | (_) | | | | \__ \ | |_) |  __/ (_| | | | (_) | (_) | | | | | |
 |____/ \___/|_| |_| |___/ |____/ \___|\__,_|_|  \___/ \___/|_| |_| |_|
                                                                       
""","""
 _   ___ _       _                
| | / (_) |     | |               
| |/ / _| |_ ___| |__   ___ _ __  
|    \| | __/ __| '_ \ / _ \ '_ \ 
| |\  \ | || (__| | | |  __/ | | |
\_| \_/_|\__\___|_| |_|\___|_| |_|

""","""
  __  __           _              ____           _                           
 |  \/  | __ _ ___| |_ ___ _ __  | __ )  ___  __| |_ __ ___   ___  _ __ ___  
 | |\/| |/ _` / __| __/ _ \ '__| |  _ \ / _ \/ _` | '__/ _ \ / _ \| '_ ` _ \ 
 | |  | | (_| \__ \ ||  __/ |    | |_) |  __/ (_| | | | (_) | (_) | | | | | |
 |_|  |_|\__,_|___/\__\___|_|    |____/ \___|\__,_|_|  \___/ \___/|_| |_| |_|
                                                                             
""","""
  __  __           _              ____        _   _                               
 |  \/  | __ _ ___| |_ ___ _ __  | __ )  __ _| |_| |__  _ __ ___   ___  _ __ ___  
 | |\/| |/ _` / __| __/ _ \ '__| |  _ \ / _` | __| '_ \| '__/ _ \ / _ \| '_ ` _ \ 
 | |  | | (_| \__ \ ||  __/ |    | |_) | (_| | |_| | | | | | (_) | (_) | | | | | |
 |_|  |_|\__,_|___/\__\___|_|    |____/ \__,_|\__|_| |_|_|  \___/ \___/|_| |_| |_|
                                                                                  
"""]
    print(titles[number_room-1])


def skip_game(reputation,day,win):
    """Checks if the reputation is less than or equal to 0; or the day is equal to 10
    -reputation: It's the reputation of the detective
    -day: It's the day of the sotyr
    -win: Indicates if you can still play or not (you reach reputation<=0 or day is 10)
    -Returns if you still can play the trial and if you can skip all the investigation"""

    skip=False
    if reputation<=0:
        win=False
        skip=True
    if day==10:
        print("It's time to go to trial")
        skip=True
    return win,skip


# Notes ##########################################################
def calculate_final_score(reputation,solved,time):
    """Calculates the final score of the player given the reputation and time spent values, and whether the case has been solved or not.
    -reputation: It's the reputation that the player have when they finish the case (0-100)
    -solved: It indicates if the case is solved (true) or not
    -time: It's the number of day that pass until you complete the investigation"""

    score=0
    if solved:
        score+=50 #passed with at least solving the case
    score+=50-5*time #time
    score+=20-(100-reputation)*2//10 #reputation
    return score

#print(calculate_final_score(90,True,0))
def create_notes():
    """Creates the files of the detective notes"""
    try:
        p=open("Notes.txt","w")

        p.write("Hi!\nThese are your notes, you can write anything you want that you think is important to remember\n")
        #f.write("Name ; Days ; Reputation ; Performance points ; Final Score\n")
    finally:
        p.close()


def read_file(name):
    """Reads a file line by file and prints each line
    -name: It's the name of the file with its extension"""

    try:
        p=open(name,"r")
        while True:
            line=p.readline()
            if line=="":
                break
            print(line)
    finally:
        p.close()


def show_notes():
    """Shows the notes of the detective and allows the detective to write something"""

    read_file("Notes.txt")
    option=input("Before continuing, do you want to write something? (yes/no)\n").strip().lower()
    if option=="yes":
        ask=input("What do you want to write?\n").strip()
        try:
            p=open("Notes.txt","a")
            p.write(ask+"\n")
        finally:
            p.close()


def write_final_score(name,days,reputation,per_points,solved):
    """Writes the final score of the detective as csv
    -name: It's the name of the detective
    -days: It's the number of days passed
    -reputation: It's the reputation of the detective
    -per_points: They are the performance points of the detective
    -solved: Indicates if you have win or not"""

    try:
        f=open("Final Scores.txt","a")
        f.write(f"{name} ; {days} days ; {reputation} reputation ; {per_points} performance ; {calculate_final_score(reputation,solved,days)} score\n")
    finally:
        f.close()
    
# write_final_score("B",1,100,100,True)
# read_file("Final Scores.txt")
# print_credits()

# Check inputs ##########################################################
def check_int(message):
    """Checks that the user introduces an integer. If not, it will be asked again
    -message: It's the message used to asked for something"""

    while True:
        x=input(message)
        if x.strip().lstrip("-").isdigit():
            return int(x)
        else:
            print("That's not a number")


def check_int_in_range(message,minimum,maximum):
    """Checks that the user introduces an integer that is in [minimum,maximum]. If not, it will be asked again
    -message: It's the message used to asked for something
    -minimum: It's the lower limit of the range (included)
    -maximum: It's the upper limit of the range (included)"""

    while True:
        x=check_int(message)
        if x>=minimum and x<=maximum:
            return x
        print(f"The number must be in [{minimum},{maximum}]")


def str_in_list(item,mylist):
    """Indicates whether a string is in a list or not, ignoring capital letters
    -item: It's the item going to be checked
    -mylist: It's the list"""

    for i in mylist:
        if item.lower()==i.lower():
            return True
    return False


# Other
def observe():
    """It returns True if the dice is 4,5 or 6, and the inspector observes something useful.
    It returns False if the dice is 1, 2 or 3, and the inspector can't determine if something is useful or not"""

    dice=random.randint(1,6)
    if dice>=4:
        return True
    return False


def ask_player_name():
    """Asks the player to input their name, It must be only 1 word and 10 characters maximum"""

    while True:
        name=input("Introduce your name (one word, ten characters maximum): ").strip()
        name_list=list(name)
        safe=True
        for let in name_list:
            if let==" ":  #the name can't be more than one word, therefore, there are no spaces
                safe=False
        if len(name_list)>10 or not safe: #ensures that the name is within the stated rules
            print("Invalid name, please introduce one within the rules")
        else:
            break
    my_name=name.lower().capitalize() #capitalizes and lower the name
    return my_name
