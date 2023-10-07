import Games
import Input_Output
import random
import characters 

def interrogation_text_init():
    """ Prints the title of this section """

    print("""
 _   _     _____  ____  ___   ___   ___   __     __   _____  _   ___   _     
| | | |\ |  | |  | |_  | |_) | |_) / / \ / /`_  / /\   | |  | | / / \ | |\ | 
|_| |_| \|  |_|  |_|__ |_| \ |_| \ \_\_/ \_\_/ /_/--\  |_|  |_| \_\_/ |_| \| 
""")
    print("\nIt's time to interrogate the suspects\n")


def choose_character_to_interrogation(dect_name):
    """Asks the player to choose who he wants to interrogate
    -dect_name: It's the name of the detective
    -Returns the person that the detective wants to interrogate"""

    while True:
        my_interrogated_one=input(f"""
{dect_name}: Who do I interrogate now?:
    - Matthew
    - Lilian
    - Veronica
    - Bob
    (Write 'Done' if you have no more questions)\n""").strip().lower()

        if my_interrogated_one=="matthew" or my_interrogated_one=="lilian" or my_interrogated_one=="veronica" or my_interrogated_one=="bob" or my_interrogated_one=="done":
            break
        else:
            print(f"{dect_name}: That makes no sense")
    return my_interrogated_one.capitalize()


def the_interrogation(dect_name, murderer):
    """List of questions and answers to all the characters and game-engine
    -dect_name: It's the name of the detective
    -murderer: It's the dictionary with all the information of the murderer"""
    
    interrogation_text_init()

    #QUESTIONS FOR ALL THE CHARACTERS IN BOTH CASES: GUILTY OR NOT (3)
    questions_to_matthew_no_guilty=["Mr. Evans, I'm very sorry about this, but as you can understand, I have a few questions to ask. By the way: nice diamond watch.",
    "After the death of your father, how has your relationship with your mother been?","Who is for you the main suspect in the murder of your mother?"]
    questions_to_lilian_no_guilty=["Mrs. Adams, my condolences. I know that you have been in the service of the deceased Madame for many years… but please understand that I must ask you a few questions.",
    "After all these years in the service of Madame, who is the main suspect in her murder for you?","Had Bob an affair with the Madame?"]
    questions_to_veronica_no_guilty=["Mrs. Smith, my condolences. I know that the Madame was your friend, but understand that I have to ask you some questions...",
    "You were Madame's best friend, right? How can you explain what happened? Do you have any suspects?","Where were you at the time of the murder?"]
    questions_to_bob_no_guilty=["Mr. Evans, I'm very sorry about this, but as you can understand, I have a few questions to ask.",
    "Let me be clear: did you have an affair with the madame?","Tell me then, who is the main suspect for you?"]

    #QUESTIONS FOR ALL THE CHARACTERS IF THEY ARE GUILTY (1)
    questions_to_guilty_matthew=["Nobody has seen you that night around the crime time, and I've seen large footprints on the grass, widely separated from each other, \n\tsurrounding the house, as if fleeing from the scene of the crime... only your feet are so big..."]
    questions_to_guilty_lilian=["Lilian, after all this time you haven't had any salary improvements, have you? The Madame died of poisoning and you are responsible for the food. This looks bad for you"]
    questions_to_guilty_veronica=["Veronica, Madame's life could be what you always wanted... some witnesses to that night see you as the murderer..."]
    questions_to_guilty_bob=["Nobody has seen you that night around the crime time. I think this was a crime of passion, you were in love with Madame and since she didn't\n\treciprocate you went crazy and killed her. Confess now and your sentence will be lower"]

    #ANSWERS FROM ALL CHARACTERS IN BOTH CASES:GUILTY OR NOT (3)
    answers_from_matthew_no_guilty=["Thank you. come on, go ahead","It has not changed. We had no problem at all","This all surprised me a lot, but I don't like Bob's attitude... Perhaps he is the murderer...I can't be sure."]
    answers_from_lilian_no_guilty=["I understand, go ahead.","I don't have a clear suspect, Veronica was very envious of Madame... although I never liked Bob's malicious behavior with Madame.","I couldn't guarantee it. but I think that's what he intended."]
    answers_from_veronica_no_guilty=["Ok, sure...","I think I could be her best friend...I'm still surprised...I don't know what to think...Lilian would like to earn so much more, Bob was crazy about her...\n\t  I guess Matthew will be destroyed...I don't have clear ideas now...",
    "I heard screaming, I was in the middle of the corridor, I don't remember where I was going, because I run immediately towards the pool"]
    answers_from_bob_no_guilty=["Let's go...","THAT IS COMPLETELY FALSE! HOW DARE YOU SAY THAT!","I believe Veronica may be the killer."]

    #ANSWERS FROM ALL THE CHARACTERS IF THEY ARE GUILTY (1)
    answers_from_guilty_matthew=["ARE YOU INTENDING THAT I AM THE MURDERER? HOW DO YOU DARE? I'M INNOCENT"]
    answers_from_guilty_lilian=["DON'T EVEN THINK ABOUT THAT! THERE HAS TO BE ANOTHER EXPLANATION. ANYONE COULD DO IT, I AM NOT THE OWNER OF THE KITCHEN...I AM NOT THE MURDERER"]
    answers_from_guilty_veronica=["I CANNOT BELIEVE IT... I HAVE ALWAYS BEEN ENVIOUS OF HER, BUT I NEVER WANTED TO KILL HER... I AM INNOCENT."]
    answers_from_guilty_bob=["I THINK I WAS IN THE BATHROOM. I WILL NEVER CONFESS SOMETHING I HAVE NOT COMMITTED!! I'M INNOCENT!! LOOK FOR THE TRUE CULPRIT!!"]

    #GAME-ENGINE
    while True:
        dect_choice=choose_character_to_interrogation(dect_name)
        if dect_choice=="Matthew":
            if murderer["name"]=="Matthew":
                total_questions=questions_to_matthew_no_guilty+questions_to_guilty_matthew
                total_answers=answers_from_matthew_no_guilty+answers_from_guilty_matthew
            else:
                total_questions=questions_to_matthew_no_guilty
                total_answers=answers_from_matthew_no_guilty

        elif dect_choice=="Lilian":
            if murderer["name"]=="Lilian":
                total_questions=questions_to_lilian_no_guilty+questions_to_guilty_lilian
                total_answers=answers_from_lilian_no_guilty+answers_from_guilty_lilian
            else:
                total_questions=questions_to_lilian_no_guilty
                total_answers=answers_from_lilian_no_guilty

        elif dect_choice=="Veronica":
            if murderer["name"]=="Veronica":
                total_questions=questions_to_veronica_no_guilty+questions_to_guilty_veronica
                total_answers=answers_from_veronica_no_guilty+answers_from_guilty_veronica
            else:
                total_questions=questions_to_veronica_no_guilty
                total_answers=answers_from_veronica_no_guilty

        elif dect_choice=="Bob":
            if murderer["name"]=="Bob":
                total_questions=questions_to_bob_no_guilty+questions_to_guilty_bob
                total_answers=answers_from_bob_no_guilty+answers_from_guilty_bob
            else:
                total_questions=questions_to_bob_no_guilty
                total_answers=answers_from_bob_no_guilty

        elif dect_choice=="Done":
            print(f"{dect_name}: Well, guess I am finished with the interrogation, let's continue!")
            break
        
        #for the message
        questions="Which question do I ask?\n"
        for i in range(0,len(total_questions),1):
            questions+=f"""\t{i+1}.- {total_questions[i]}\n"""
        
        tries=len(total_questions)
        while tries>0:
            print(f"\n\nChoose the question to be asked, you have {tries} questions left: ")
            q=Input_Output.check_int_in_range(questions,1,len(total_questions))
            # i+1=q
            a=total_questions[q-1]
            b=total_answers[q-1]
            print(f"\n{dect_name}: {a}")
            print(f"{dect_choice.capitalize()}: {b}")
            tries-=1


#############################################################################################
#dect_name=Input_Output.ask_player_name()
#murderer=Input_Output.sus_selection()
#the_interrogation(dect_name,murderer) 

def random_event(reputation,room_number,murderer,suspects):
    """It returns a clue randomly that can be true or not. The clue is from the rooms before
    -reputation: It's the reputation of the detective
    -room_number: It's the number of the room (1.outside,2.office....)
    -murderer: It's the dictionary with all the murderer's information
    -suspects: It's a dictionary with all the suspects' information"""
    # if room_number<4:
    #     return None
    rooms=["weapon","motive","casino","library","living","son's","kitchen","bedroom","bathroom"]
    clues=rooms[0:room_number]
    clue=clues[random.randint(0,len(clues)-1)]
    if clue=="casino" or clue=="bathroom":
        return None
    if reputation+random.randint(0,20)<20:
        event=characters.return_clue(murderer,suspects,clue)
    elif random.randint(0,20)>18:
        event=murderer[clue]
    else:
        return None
    print(f"*** \nAfter closing the door I see a note in the floor just saying:'{event}' \nI don't now if I can trust this but may be useful\n***")
 

def pool(energy,reputation,murderer,suspects,rooms,day):
    """It's the 1st room
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(1)
    print("""I am in the crime scene, this is a huge space, this party maybe could be able to hold 200 people. The killer could be anyone.
\tThe only things left are some bottles left on the grass; a cocktail bar with some glasses around; the pool with lights turn off; and some blood and vomit
of the victim""")
    while True:
        zone=Input_Output.check_int_in_range("""\nWhich zone should I investigate? 
    1. Bottles
    2. Cocktail Bar
    3. Pool
    4. Blood and vomit\n""",1,4)
        #check energy and reputation?
        if zone==1:
            print("I go to the zone and there are some broken bottles, other ones half full")
            if Input_Output.observe():
                print("Definitely, this is only trash")
            else:
                print("I don't know if this could be useful")
        
        elif zone==2:
            print("""In the bar are 3 shelves with 3 glasses on each but one glass seems to be missing. There are also some glasses disorganized around the bar.
All the glasses have different drawings on each""")
            if Input_Output.observe():
                print("I think the glasses have some relation between them")
                energy,reputation,day,win=Games.play_psycho(energy,reputation,day)

                print("After putting the glass in the position, a cupboard opens. ")
                if win:
                    weapon=murderer["weapon"]
                    text="I am sure"
                else:
                    weapon=characters.return_clue(murderer,suspects,"weapon")
                    text="I think"
                
                if weapon=="Pushed" or weapon=="Strangled":
                    print(f"""But before I see what's there. I receive a message from the forensic surgeon:
-The only thing I can tell you now is that {text} Madame was {weapon}""")
                    print("After this information, let's see what's in the cupboard.\nOh, there is a note with the code for the next room:",rooms["Outside"])
                else:
                    if weapon=="Poison":
                        print(f"In the cupboard, there is a glass half-full with a strange color. I smell it, it's disgusting. {text} that Madame was poisoned")
                    else:
                        print(f"In the cupboard, there is a knife with blood on it. {text} this is the weapon of the murder")
                    print("There is also a note with the code for the next room:",rooms["Outside"])
                break
            else:
                print("I don't know if this could be useful")
        
        elif zone==3:
            print("The pool is huge but i can't see if there is something at the bottom, because it's very dark")
            if Input_Output.observe():
                print("With a lantern illuminate the bottom of the pool, and I see that there is only trash")
            else:
                print("I don't know if this could be useful")
        
        elif zone==4:
            print("""There is a sign pointing out that here was where the corpse was. There is all over the place vomit mixed with blood, maybe she was poisoned or
she feel sick after too many drinks""")
            if Input_Output.observe():
                print("Definitely this is not useful, and I will have to wait for the autopsy")
            else:
                print("I don't know if this could be useful")
        
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day


def casino(energy,reputation,murderer,suspects,rooms,day):
    """It's the 4th room
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(4)
    print("""Another room, when this is going to end?
I am surprised that there is a casino in this house, I doubt that a real one is as luxurious as this one. Everything looks like gold with some red details.
There is huge billiard table; a red carpet with a strange fold; a small screen off; and a slot machine with the glass broken""")
    while True:
        zone=Input_Output.check_int_in_range("""\nWhich zone should I investigate? 
    1. Billiard table
    2. Red carpet
    3. Small screen
    4. Slot machine\n""",1,4)
        #check energy and reputation?
        if zone==1:
            print("When I go near, I see something shiny. It could be a weapon.")
            if Input_Output.observe():
                print("I found a gap, it was just a ring that someone has lost. Obviously, it's not useful")
            else:
                print("I forgot where it was the shining, I should keep searching")
        
        elif zone==2:
            print("""In the zone of the fold, I lift the carpet and I see a trapdoor.""")
            if Input_Output.observe():
                print("Finally, I was able to open it and it's just a warehouse for the casino. Besides, the old machines, there is nothing useful")
            else:
                print("I try to  open it but seems to be block, I should make an effort to open it")
        
        elif zone==3:
            print("""The screen has the wires damaged, I don't for what is it""")
            if Input_Output.observe():
                print("After a while, the screen turns on. In the screen a card game appears with 2 buttons: higher and lower")
                energy,reputation,day,win=Games.play_cards(energy,reputation,day)   
                
                if win:
                    fight=murderer["name"]
                else:
                    fight=characters.return_clue(murderer,suspects,"name")
                print(f"""Suddenly, a video appears. There is Madame and {fight}, arguing about something.
I cannot know why they are fighting, there is no audio, but {fight} is losing his/her cool.
That could be an explanation of the slot machine, but fighting with someone makes you a murderer?\n""")
                print("After the video ends, a text appears:",rooms["Casino"],". It's the code for the next room.")
                break
            else:
                print("I try to join them together , but I don't know if I am making it worse")
        
        elif zone==4:
            print("It seems like there was a fight or someone was piss off by their bad streak")
            if Input_Output.observe():
                print("Besides calling to the cleaning service, I should investigate other things")
            else:
                print("I don't know if this could be useful")
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day


def living_room(energy,reputation,murderer,suspects,rooms,day):
    """It's the 5th room
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(5)
    print("""Now, the living room. Although it's luxurious, it gives you a cozy feeling. It has a large window with a beautiful view of the garden.
Moreover, there is a big white couch, a carpet under it, a modern fireplace and some shelves with the expensive dinnerware set""")
    while True:
        zone=Input_Output.check_int_in_range("""\nWhich zone should I investigate? 
    1. White couch
    2. Carpet
    3. Shelves
    4. Fireplace\n""",1,4)
        if zone==1:
            print("Maybe there is something hiding between the cushions")
            if Input_Output.observe():
                print("I move every cushion and there is nothing")
            else:
                print("At first sight I don't see anything, I should search more")
        
        elif zone==2:
            print("There is a carpet under the couch, and the only visible thing is a part of the print")
            if Input_Output.observe():
                print("I could move it, and the print looks like a strange riddle")
                energy,reputation,day,win=Games.play_flw(energy,reputation,day)

                print("When I try to put the couch on the place, I see 2 notes: one is crumpled note and one little note\nFirst, I take the crumpled note. Oh..")
                if win:
                    note=murderer["living"]
                else:
                    note=characters.return_clue(murderer,suspects,"living")
                print (f"It's a {note} Interesting.\nThe other note is the code for the next room:",rooms["Living Room"])
                break
            else:
                print("I try to move the couch but it's too heavy, I need to push more")
        
        elif zone==3:
            print("Like in any other expensive house, the most expensive dinnerware set of the house is shown")
            if Input_Output.observe():
                print("Moving carefully the plates and glasses, there is nothing hidden. I should not touch them any more")
            else:
                print("At first sight I don't see anything, I should search more")
        
        elif zone==4:
            print("The fireplace is still warm, someone lit it. There is something burnt in there")
            if Input_Output.observe():
                print("Carefully, I take it out, it's just an illegible paper. Now, it's only trash")
            else:
                print("Trying to take it out, I burn my hand. I should wait a bit")
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy, reputation,day


def master_bedroom(energy,reputation,murderer,suspects,rooms,day):
    """Plays the events happening in the master bedroom (8th room)
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(8)
    print("""I open Madame's bedroom door. It's truly spacious, fancy and organized.
Madame must have cared a lot about keeping everything presentable. At first glance, some things catch my attention: a computer, a portrait of Madame with
her cats, a purse hanging in a chair, and a bright red book on a shelf.""")
    while True:
        zone=Input_Output.check_int_in_range("""\nWhich one should I investigate?
    1. Computer
    2. Portrait
    3. Purse
    4. Book\n""",1,4)
        if zone==1:
            print("I go to the computer, and it is shutted down, as expected.")
            if Input_Output.observe():
                print("Let's try guessing the password. Three letters, kinda short...\n...")
                print("The password asks for three letters, and there's a little clue: \n*SHORTLY, what I love the most*\n")
                password() #<-This minigame does not affect the energy and the reputation

                energy,reputation,day,win=Games.play_math_secuence(energy,reputation,day)
                print("After completing the game, 2 codes appear on the screen:")
                print("DOOR :",rooms["Master Bedroom"])
                print("VAULT: MADAME")
                print("""\nI search for the vault all over the bedroom and, in the closet, under her clothes, I see the vault. I put the code, and inside of 
there is a diary. I open the diary in a random page and I see:""")
                if win:
                    note=murderer["bedroom"]
                else:
                    note=characters.return_clue(murderer,suspects,"bedroom")
                print(note)
                print("I should better go to the next room instead of invading her privacy")
                break
            else:
                print("I don't know if looking here is worth it.")

        elif zone==2:
            if Input_Output.observe():
                print("I am surely losing time looking here.")
            else:
                print("I don't know if looking here is worth it.")
        elif zone==3:
            if Input_Output.observe():
                print("I am surely losing time looking here.")
            else:
                print("I don't know if looking here is worth it.")
        elif zone==4:
            if Input_Output.observe():
                print("I am surely losing time looking here.")
            else:
                print("I don't know if looking here is worth it.")
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day


def password():
    """Minigame to guess Madame's password"""
    clues=["It may be the initials of two things","The middle letter must be '&'.",
"Her cats were named Diamond and Coco, then it is D and C right?"]
    tries=0
    while True:
        if clues!=[]:
            clue=clues.pop(random.randint(0,len(clues)-1))
        else:
            print("All clues have been already granted.")

        password="D&C".lower()
        pw=input("Introduce the password: ").strip().lower()
        if pw=="mat":
            print("So it is not the son huh?")
        
        elif pw==password:
            print("Done! It was the cats!\n")
            break
        else:
            print("Tough luck.")
        
        if clue!="":
            print(f"The computer gives you a clue: {clue}\n")
            tries+=1

        if tries>=10:
            print("After trying for a long... long time, you notice a paper with the password laying in the table, it is D&C.\n")


def library(energy,reputation,murderer,suspects,rooms,day):
    """Plays the events that occur in the library (3rd room)
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(3)
    print("""I enter the library. It looks classy, but most importantly, well organized. It is kinda big, but the huge windows let the light bright the
    room perfectly for a reading session.
    Some things quickly catch my attention: a book left in the corner, an old-looking shelf, the previously mentioned windows, and the lamp""")

    while True:
        zone=Input_Output.check_int_in_range("""\nWhich one should I investigate?
    1. Book
    2. Shelf
    3. Windows
    4. Lamp \n""",1,4)
        if zone==1:
            print("I decide to investigate the book.")
            if Input_Output.observe():
                print("I read a bit. It was a philosophy book. I left it where it was and didn't look back.")
            else:
                print("I don't know if there is anything interesting here.")

        elif zone==2:
            print("I go to the shelf...")
            if Input_Output.observe():
                print("...and after a while I noticed a pretty little light coming from behind it.")
                print("I put some stuff away and guess what I found...\nA SAFE!")
                energy,reputation,day,win=Games.lever_game(energy,reputation,day)
                if win:
                    print("I succesfully solve the lever game, opening the safe...")
                    clue=murderer["library"]
                    print(f"...and, apart from what you would expect, I notice {clue.lower()} \nI am sure this will be a crucial detail.")
                else:
                    clue=characters.return_clue(murderer,suspects,"library")
                    print(f"but, as if it was a matter of luck, I notice {clue.lower()} near the safe \nI think this could be something important.")
                print("Oh, there is also a paper with the code of the next room",rooms["Library"])
                break
            else:
                print("... but I don't really know if there is anything interesting here.")

        elif zone==3:
            if Input_Output.observe():
                print("The view is truly amazing, no one could ever deny that, but I am pretty sure I won't find anything here.")
            else:
                print("I don't know if there could be anything useful here")
        elif zone==4:
            print("I go to investigate the lamp")
            if Input_Output.observe():
                print("Looking up to the ceiling as a fool, I realize I won't find anything useful staying like this.")
            else:
                print("I don't know whether there is something interesting there or not.")

        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day

#library(20,100,characters.lilian,characters.suspects,Input_Output.assign_keys(Input_Output.list_rooms),0)


def kitchen(energy,reputation,murderer,suspects,rooms,day):
    """Plays the events that occur in the kitchen (7th room)
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(7)
    print("""I enter the kitchen. It is truly lovely. Although it is above the average person's means, it also has that warm feeling every kitchen
should have. Some things catch my attention: the sink, the fridge, the tiles of the floor, and the oven.""")
    while True:
        zone=Input_Output.check_int_in_range("""\nWhich one should I investigate?
    1. Sink
    2. Fridge
    3. Tiles
    4. Oven \n""",1,4)
        if zone==1:
            print("I go to investigate the sink.")
            if Input_Output.observe():
                print("This is surely a waste of time")
            else:
                print("I don't know if there is anything valuable here")
        elif zone==2:
            print("I open the fridge... \nTHEY HAVE A LOT OF FOOD! I am kinda hungry, should I pick something?")
            pick=input("Should you? (yes or no)\n").strip().lower()

            if pick=="yes":
                print("\nOne bite won't hurt...\nThere's a chocolate milkshake, an apple, and a yogurt.\n")
                food=input("""What should I grab?
    1. Milkshake
    2. Apple
    3. Yogurt \n""").strip()
                if food=="1":
                    print("You finish your delicious milkshake pretty quickly...\nThat was a nice treat.")
                elif food=="2":
                    print("You take a bite of the apple...\nIt's disgusting! It must have rotted!!!")
                elif food=="3":
                    print("You take the yogurt...\n...but you realise that you will also need an spon, so you decide to leave it behind")
                else:
                    print("Nah, better if I not touch anything")

            elif pick=="no":
                print("I shouldn't touch anything...")

            else:
                print("You weren't sure if a milkshake was worth breaking the rules of \nnot touching anything in the crime scene...")
            print("Forget it, there is nothing useful here, let's continue")

        elif zone==3:
            print("I lean down in order to see them closely...")
            if Input_Output.observe():
                print("Wait! There is something going on here!")
                energy,reputation,day,win=Games.play_CC(energy,reputation,day)
                if win:
                    clue=murderer["kitchen"]
                    print(f"I successfully solve the game of the tiles...\n...and I suddenly notice that {clue} \nI am sure this will be a crucial detail.")
                else:
                    clue=characters.return_clue(murderer,suspects,"kitchen")
                    print(f"At least I tried...\n...and I suddenly notice that {clue}\nI think this could be something important")
                print("Oh, there is also a paper with the code of the next room",rooms["Kitchen"])
                break

            else:
                print("I don't know if there could be anything useful here")
        elif zone==4:
            print("I go to investigate the oven.")
            if Input_Output.observe():
                print("It smells nice, must be for the food of the party, but I won't find anything useful here.")
            else:
                print("I don't know if there is anything valuable here.")

        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)        
    return energy,reputation,day


#kitchen(20,100,characters.lilian,characters.suspects,Input_Output.assign_keys(Input_Output.list_rooms),0)


def the_office(energy,reputation,murderer,suspects,rooms,day):
    """This is the office (2nd room) definition and game-engine
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    Input_Output.print_rooms(2)
    print("""The office is spacious and luxuriously furnished. A large window illuminates the room, in the center of which there is a large office 
table, with a large boss's chair behind it. The walls have hardwood shelves full of books, on the topics that most interested the deceased husband 
of the victim. The central table has only one drawer...\n""")
    while True:
        zone=Input_Output.check_int_in_range("""What do you choose to investigate?
    1.- Check the books on the shelf
    2.- Check the main table\n""",1,2)

        if zone==1:
            if Input_Output.observe():
                print("""I have gone through the books and found one poetry book that caught my attention. It is a book with more signs of use. It's
pretty worn out and in it I found this MORSE code table: \n
    -The space between letters is 3 units
    -The space between words is 7 units
    A   ● ▂         N   ▂ ●          0   ▂ ▂ ▂ ▂ ▂
    B   ▂ ● ● ●     O   ▂ ▂ ▂        1   ● ▂ ▂ ▂ ▂
    C   ▂ ● ▂ ●     P   ● ▂ ▂ ●      2   ● ● ▂ ▂ ▂
    D   ▂ ● ●       Q   ▂ ▂ ● ▂      3   ● ● ● ▂ ▂
    E   ●           R   ● ▂ ●        4   ● ● ● ● ▂
    F   ● ● ▂ ●     S   ● ● ●        5   ● ● ● ● ●
    G   ▂ ▂ ●       T    ▂           6   ▂ ● ● ● ●
    H   ● ● ● ●     U   ● ● ▂        7   ▂ ▂ ● ● ●
    I   ● ●         V   ● ● ● ▂      8   ▂ ▂ ▂ ● ●
    J   ● ▂ ▂ ▂     W   ● ▂ ▂        9   ▂ ▂ ▂ ▂ ●
    K   ▂ ● ▂       X   ▂ ● ● ▂      .   ● ▂ ● ▂ ● ▂
    L   ● ▂ ● ●     Y   ▂ ● ▂ ▂      ,   ▂ ▂ ● ● ▂ ▂
    M   ▂ ▂         Z   ▂ ▂ ● ●      ?   ● ● ▂ ▂ ● ●\n""")
                print("I think I will go check the main table now...") #I now it looks disorganized but in the print its perfect
            else:
                print("There are a lot of books, I don't know where to start")
    
        elif zone==2:
            print("""I am going to check the main table...\nIt's strange that such a big table only has one drawer...
It has been difficult to open it, and I only see inconsequential papers...\nThere could be something else here... I'm going to hit it...""")
            #Next, a condition is requested to hit the drawer.
            #But it will be a matter of fortune that you hit it hard enough to break it.
            #Depending on this, your options will change
            hit=Input_Output.check_int("If you want to hit the drawer hard, write an integer number > 10: ")
            #esto se puede hacer con un numero random para que lo venzas, y yo haría que puedieras seguir golpeando, pero como veais
            if hit>10:
                print("""You have hit this drawer... But you don't know if you've hit it hard enough:
If so you won't discover anything interesting, otherwise you might find something useful...\n...\n""")
                if Input_Output.observe():
                    print("""Good Luck!, your hit has been hard enough!\nThere is a false bottom in this drawer!!\nYou just found a possible clue here:""")
                    #HERE THE MORSE GAME BEGINS (if the condition is met)
                    energy,reputation,day,win=Games.play_morse(energy,reputation,day,murderer)
                    if not win:
                        clue=characters.return_clue(murderer,suspects,"motive")
                        print(f"Well, I am not really good at this I think it says: {clue}. That might be a good motive for a crime")
                else:
                    print("Bad luck! It won't open.\nYou leave the room thinking about gym memberships.")
                    reputation-=5
            else:
                print("You haven't hit the drawer hard enough. You have to get out of this room.")
                reputation-=5
            print("A note fells of the drawer because of the hit, it has the code for the next room:",rooms["Office"])
            break
                
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day


def the_sons_bedroom(energy,reputation,murderer,suspects,rooms,day):
    """This is the son's bedroom (6th room) definition
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""


    Input_Output.print_rooms(6)
    print("""This room is ridiculously big, even though there's no much inside of it: a bed, which is big enough for an adult to sleep in, the
lights, a shelf with some books... and the standard bedroom stuff that's pretty much it.\n\nLet's investigate...""")

    #Object's choice to be investigated
    while True:
        item=Input_Output.check_int_in_range(f"""\nWhere do you think Matthew would hide his secrets?
    1.- On the hanging lamp
    2.- On that little shelf with a few books
    3.- Under the bed\n""",1,3)

        #hanging lamp investigation process:
        if item==1:
            print("""Through the translucent crystals of the hanging lamp, it can be seen that there is something inside...\n""")
            lamp=0
            while lamp<3:
                crystal_removed=Input_Output.check_int_in_range("""I am going to remove the following crystals:
    1.- remove the green crystal
    2.- remove the orange crystal
    3.- remove the white crystal
Be careful, you can remove any piece only 3 times\n\n""",1,3)
                if crystal_removed==1:
                    print("Argh!, there was a black spot, and it was a huge dead beetle.\n")
                elif crystal_removed==2:
                    print("Oops!, I saw a black spot that was a sock.\n")
                elif crystal_removed==3:
                    print("Whoops, the piece of paper that was here has fallen on the shelf with the books!!\n")
                lamp+=1
                if lamp<2: #To not subtract twice at the end after the 3rd move
                    energy-=1
                    energy,day=Input_Output.check_energy(energy,day)
                    Input_Output.print_status(energy,reputation)

        #Shelf with books investigation process:
        elif item==2:
            print("There are some books in here, let's go through them.")
            if Input_Output.observe():
                print("Nah, this isn't useful at all.")
            else:
                print("I don't know whether this is useful or not.")

        #Under the bed investigation process:
        elif item==3:
            print("""There is a book inside what appears to be a little treasure box. It is a child's stories book that Matthew's late father has
left dedicated to his son. In it, I could find something interesting...\n""")
            energy,reputation,day,win=Games.quizz_engine(energy,reputation,day)
            print("""\nWhat's this? \n\n*You find something written at the end of the book.* \nUhm, it is almost unreadable... but I think I can understand this:\n""")
            if win:
                print("It says:",murderer["son's"])
            else:
                text=characters.return_clue(murderer,suspects,"son's")
                print(f"It says: {text} \nI wouldn't trust this lead that much...\n")

            print("When I close the book, a note fell, it's the code for the next room",rooms["Son's Bedroom"])
            print("You can leave this room.")
            break
        energy-=1
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day


def the_bathroom(energy,reputation,murderer,day):
    """This is the bathroom (9th room) definition
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -murderer: It's the dictionary of the murderer
    -suspects: It's a dictionary with all the suspects' information"
    -rooms: The dictionary with each room and its key"
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""
    
    death=False
    Input_Output.print_rooms(9)
    print("""I'm going into the bathroom, it's not very big, considering the rest of the house. It is dominated by the imposing presence of a
large, gloomy mirror. 
The large bathtub has four taps! It could have been a good place to dismember the corpse...
There is a small dresser with 3 drawers, red, yellow and green under the sink, it looks like a traffic light!
The toilet is strange. It has a button panel to its left, located at the end of a pedestal almost three feet high...""")

    #Object's choice to be investigated:
    while True:
        item=Input_Output.check_int_in_range(f"""\nWhich item should I investigate?
    1. Bathtub
    2. Mirror
    3. Dresser
    4. Toilet\n""",1,4)

        #Bathtub investigation process:
        if item==1:
            print("""There is something inside the water outlet pipe... I will try to extract it by opening the faucet and, in this way, the water
will help me...but I do not know why this bathtub has 4 taps...\nI will try to open one...\n""")
            tap=0
            while tap<=3:
                tap_to_be_openned=Input_Output.check_int_in_range("""I am going to choose this tab to be opened:
    1.- open top left tap
    2.- open left tap
    3.- open right tap
    4.- open top right tap\n""",1,4)
                if tap_to_be_openned==1 or tap_to_be_openned==2:
                    print("Oops!, This tap doesn't work\n")
                elif tap_to_be_openned==3:
                    print("My God, what strange sound... but no watter\n")
                elif tap_to_be_openned==4:
                    print("""The water has extracted a piece of cloth... there's something written here... uhmm... it says... "keep looking".\n""")
                tap+=1
                if tap<3: #To not subtract twice at the end after the 4rd move
                    energy-=1
                    energy,day=Input_Output.check_energy(energy,day)
                    Input_Output.print_status(energy,reputation)

        #Mirror investigation process:
        elif item==2:
            print("""This mirror is so sinister...OMG! When turning on the hot water tap in the sink it fogs up, something or someone has written on it:
'PLAY HANGMAN!'\n""")
            word=Games.hangman_word_generator()
            Games.hangman_init_text(word)
            energy,reputation,day,win=Games.hangman_play(energy,reputation,day,word)

            if win:
                print("""\nI was saved from dying in the terrible Hangman game!! As the mirror has been demisted, I have been able to see reflected in it the murderer who was going to kill me too!!
The killer ran across very quickly, but I could clearly see that the killer is: """)
                print("A",murderer["gender"].upper(),"!!!")
            else:
                print("YOU DIED... what a pity. You were killed by",murderer["name"])
                energy=2
                reputation=0
                death=True
            break

        #Dresser investigation process:
        elif item==3:
            drawer=0
            while drawer<=2:
                drawer_to_be_openned=Input_Output.check_int_in_range("""I'll try to see if I have more luck with the drawers... there might be some clues inside them...
    1.- open the red drawer
    2.- open the yellow drawer
    3.- open green drawer\n""",1,3)
                if drawer_to_be_openned==1 or drawer_to_be_openned==3:
                    print("This drawer is empty...")
                else:
                    print("""Inside this drawer there are only some bars of soap... from the brand "keep looking".\n""")
                drawer+=1
                if drawer<2: #To not subtract twice at the end after the 3rd move
                    energy-=1
                    energy,day=Input_Output.check_energy(energy,day)
                    Input_Output.print_status(energy,reputation)

        #Toilet investigation process:
        elif item==4:
            toilet=0
            while toilet<=2:
                toilet_buttons=Input_Output.check_int_in_range("""After seeing that creepy mirror I had to use the toilet.
Now I am going to use its modern button panel... which one should I press?
    1.- press button #1
    2.- press button #2
    3.- press button #3\n""",1,3)
                if toilet_buttons==1:
                    print("Boiling water on my butt!!!!\n")
                if toilet_buttons==2:
                    print("Fress water on my butt!!!!\n")
                if toilet_buttons==3:
                    print("Very annoying explosion in the toilet!!!!\n")
                toilet+=1
                if toilet<2: #To not subtract twice at the end after the 3rd move
                    energy-=1
                    energy,day=Input_Output.check_energy(energy,day)
                    Input_Output.print_status(energy,reputation)

    energy-=1
    energy,day=Input_Output.check_energy(energy,day)
    if death==True:
        energy=0
        reputation=0
    Input_Output.print_status(energy,reputation)
    print("You can leave the bathroom")
    return energy,reputation,day,death