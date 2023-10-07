import random
import Input_Output
import characters

def check_int_MMCM(message):
    """It asks for a number and checks if it's a number or MMCM (cheats mode)
    -message:It's the message used to asked for something"""

    while True:
        number=input(message).strip()
        if number.lstrip("-").isdigit():
            return int(number)
        if number.lower()=="mmcm":
            print("CHEATS MODE ACTIVATED")
            return number.lower()
        print("That's not a number")


def check_int_MMCM_in_range(message,min,max):
    """It asks for a number in [min,max] and checks if it's a number in [min,max] or MMCM (cheats mode)
    -message:It's the message used to asked for something
    -minimum: It's the lower limit of the range (included)
    -maximum: It's the upper limit of the range (included)"""

    while True:
        number=check_int_MMCM(message)
        if number=="mmcm":
            return number
        if number>=min and number<=max:
            return number
        print(f"The number must be in [{min},{max}]")


# Caesar Cypher ######
def romano(message):
    """Creates an encrypted message from a given one moving all the letters a random number of positions
    -message: It's the message to be encripted
    -Returns the encrypted message and the number of positions moved"""

    message=message.lower()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    positions=random.randint(1,len(alphabet)//2)
    encrypt=""
    for i in range (0,len(message),1):
        if message[i]==" " or message[i]=="," or message[i]=="." or message[i]==";":
            symbol=message[i]
            encrypt+=symbol
            continue
        for j in range (0,len(alphabet),1):
            if message[i]==alphabet[j]:
                if j+positions>=len(alphabet):
                    encrypt+=alphabet[positions-(len(alphabet)-j)]
                    break
                encrypt+=alphabet[j+positions]
                break
    return encrypt,positions #the positions you must count form right to left to guess the letter


def cc_init_txt():
    """Prints the instructions for the Caesar Cypher minigame"""

    print("\nThere are 3 encrypted messages, and I also have a number for each of them...\nWhenever I fail, the game ends...")
    print("\nI think the number may be the POSITIONS TO THE RIGHT the letter has been moved in the alphabet.\n...the alphabet huh?")
    print("I still remember the tune...\n♪A ♪B ♪C ♪D ♪E ♪F ♪G ♪H ♪I ♪J ♪K ♪L ♪M ♪N ♪O ♪P ♪Q ♪R ♪S ♪T ♪U ♪V ♪W ♪X ♪Y ♪Z\n\n")


def play_CC(energy,reputation,day):
    """Plays the Caesar Cypher minigame
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    message_list=["blood","pizza","lettuce","sadness","disgust","rich","cake", "memory","sorry","regret","alcohol","luxury","food",
    "bacon","coconut","biscuit", "chocolate"]
    guesses=3
    wins=0
    win=True
    while True:
        cc_init_txt()
        my_msg=message_list.pop(random.randint(0,len(message_list)-1))
        encrypt,positions=romano(my_msg)
        print(f"*You have to solve {guesses} words correctly. If you fail once you lose.*\n")
        print(f"This is your message to decrypt: {encrypt}\n...and this is the number: {positions}")
        guess=input("What does the message mean?").strip().lower()
        energy-=1
        if guess=="mmcm":
            print("CHEATS MODE ACTIVATED")
            wins+=1

        elif guess==my_msg:
            print("CORRECT!")
            wins+=1
        else:
            print("YOU LOST!")
            reputation-=5
            win=False
            break
        if wins==guesses:
            print("YOU'VE WON THIS GAME")
            break
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)

    energy,day=Input_Output.check_energy(energy,day)
    Input_Output.print_status(energy,reputation)
    return energy,reputation,day,win


# Morse ######
def morse(message):
    """Transforms a message into morse code. A space between letters is 3 spaces, and a space between words is 7 spaces.
    -message: It's the message to be encrypted"""

    message=message.lower()
    #the first one is the space between words
    alphabet={
    " ": "    ",       "a":"● ▂",
    "b":"▂ ● ● ●",    "c":"▂ ● ▂ ●",
    "d":"▂ ● ●",      "e":"●", 
    "f":"● ● ▂ ●",    "g":"▂ ▂ ●",
    "h":"● ● ● ●",     "i":"● ●", 
    "j":"● ▂ ▂ ▂",   "k":"▂ ● ▂",
    "l":"● ▂ ● ●",     "m": "▂ ▂",
    "n":"▂ ●",         "o":"▂ ▂ ▂",
    "p":"● ▂ ▂ ●",    "q":"▂ ▂ ● ▂",
    "r":"● ▂ ●",       "s":"● ● ●",
    "t":"▂",           "u":"● ● ▂",
    "v":"● ● ● ▂",     "w":"● ▂ ▂",
    "x":"▂ ● ● ▂",    "y":"▂ ● ▂ ▂",
    "z":"▂ ▂ ● ●"}
    encrypted=""
    for i in range(0,len(message),1):
        encrypted+=alphabet[message[i]]+"   " #after each letter i add 3 spaces
    return encrypted


def play_morse(energy,reputation,day,murderer):
    """It's the function for playing the morse
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -murderer: It's the dictionary of the murderer
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    morse_code=morse(murderer["motive"]) #encrypts the motive
    print(f"This is the word you have to decrypt. You have two chances:\n{morse_code}\n")
    chances=0
    win=True
    while True:
        safe=True
        solution=input("Write your answer:\n").strip().lower()
        for i in list(solution):
            if i==" ": #if the motive is only one word
                safe=False
        energy-=1

        if solution=="mmcm":
            print("CHEATS MODE ACTIVATED")
            break
        elif solution==murderer["motive"].lower():
            print("CORRECT!")
            print(f"Hmm, I think '{solution.upper()}' would make a good motive for a crime.")
            print("Satisfied with your work, you leave the room.")
            break
        elif safe==False:
            print("Ah, it's only ONE word!")
            print("*Please, this time write only one word*")
        else:
            print("Wrong")
            chances+=1
            if chances==2:
                print("You guessed incorrectly twice, leave")
                reputation-=5
                win=False
                break
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day,win


# Math secuences ###
def math_secuence():
    """Creates a full math sequence that chooses randomly the number you start, the operator and what amount you add/multiply"""

    operators=['+','*']
    operator=operators[random.randint(0,len(operators)-1)]
    numbers=random.randint(3,5) #number of numbers in the sequence
    start=random.randint(1,20) #number at the sequence start
    add=random.randint(-10,10)
    sequence=[]
    for i in range (0,numbers,1):
        if i==0:
            number=start
        if operator=='+':
            sequence.append(number+add)
        elif operator=='*':
            sequence.append(number*add)
        number=sequence[i]
    return sequence


def play_math_secuence(energy,reputation,day):
    """It's the function for playing the math sequence
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    guesses=0
    print("""You have three tries to guess the next number correctly per sequence, and you'll be given 3 sequences in total.
If you lose the game (failing in guessing a number in one sequence), you'll need to access the game again until you win.""")
    while True:
        tries_game=0
        secuence=math_secuence()
        win=True
        unknown=secuence.pop(-1)
       
        print("A wild mathematical sequence has appeared!")
        while True:
            for i in range (0,len(secuence),1):
                print(secuence[i],", ",end="")
                if i==len(secuence)-1:
                    print("?")

            my_guess=check_int_MMCM("Introduce your guess: ")
            energy-=1
            if my_guess=="mmcm":
                guesses=3
                break
            elif my_guess==unknown:
                print("Correct!")
                print()
                guesses+=1
                Input_Output.print_status(energy,reputation)
                break
            else:
                print("That's wrong!")
                print()
                tries_game+=1
                if tries_game==3:
                    reputation-=5
                    Input_Output.print_status(energy,reputation)
                    break
            energy,day=Input_Output.check_energy(energy,day)
            Input_Output.print_status(energy,reputation)
                
        if guesses==3:
            print("YOU WON!")
            break
        elif tries_game==3:
            print("YOU LOST!")
            reputation-=5
            break
    Input_Output.print_status(energy,reputation)
    return energy,reputation,day,win


# Lever game ###
def print_state_lever(lever):
    """It prints if a lever is on or off depending on the state
    -lever: It's a dictionary with the name and state of the lever"""
    if lever["state"]:
        print("The",lever["name"],"lever is on")
    else:
        print("The",lever["name"],"lever is off")


def check_solution(r,b,y,light):
    """Checks if the levers makes the color of the light
    -r: It's the dictionary of the red lever with its name and its state
    -b: It's the dictionary of the blue lever with its name and its state
    -y: It's the dictionary of the yellow lever with its name and its state
    -light: It's the color of the light"""

    #calculates for all the lights if it's correct or not the combination to create them
    lights={
    "red": r["state"] and not b["state"] and not y["state"],
    "yellow": y["state"] and not b["state"] and not r["state"],
    "blue":b["state"] and not r["state"] and not y["state"],
    "green": not r["state"] and b["state"] and y["state"],
    "orange": r["state"] and not b["state"] and y["state"],
    "black": r["state"] and b["state"] and y["state"],
    "purple": r["state"] and b["state"] and not y["state"] }

    if lights[light]: #Then I only check if the light that I am interested is True or False
        return True
    print("WRONG ANSWER")
    return False


def lever_game(energy,reputation,day):
    """It's the function for playing the lever game
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    lights=["red","yellow", "blue", "green", "orange","black","purple"]
    red={"name":"red", "state":False} #state-false: lever down(off)
    blue={"name":"blue", "state":False}
    yellow={"name":"yellow", "state":False}
    print("You have to solve one light. You have only 3 tries.\n")

    win=True
    tries=0
    for i in range(0,1,1): #number of plays
        light=lights[random.randint(0,len(lights)-1)] #pciks a random light
        print(f"You see a {light} light")
        while True:
            print_state_lever(red)
            print_state_lever(blue)
            print_state_lever(yellow)
            print("__________")
            option=check_int_MMCM_in_range("""What do you want to do? 
    1. Activate the red lever
    2. Activate the blue lever
    3. Activate the yellow lever
    4. Press the button
    """,1,4)
            if option=="mmcm":
                break
            if option==1:
                red["state"]=not red["state"]
            elif option==2:
                blue["state"]=not blue["state"]
            elif option==3:
                yellow["state"]=not yellow["state"]
            elif option==4:
                energy-=3
                if check_solution(red,blue,yellow,light):
                    energy,day=Input_Output.check_energy(energy,day)
                    Input_Output.print_status(energy,reputation)
                    break
                else:
                    tries+=1
                    reputation-=5
                    if tries==3:
                        win=False
                        break
                energy,day=Input_Output.check_energy(energy,day)
                Input_Output.print_status(energy,reputation)
            else:
                print("That's not an option")
        if tries==3:
            break
    return energy,reputation,day,win


#lever_game(20,100,1)
#Psychotechnical test ###
def psycho_test():
    """Returns one of the test with one unknown as list, the solution of the test and the set of options to choose as a list"""

    tests={
    0:["↘","←","←","↓","←","↑","→","→","↑"],
    1:["●","△","▲","▲","○","●","■","□","■"],
    2:["△","◮","▲","▲","△","◮","◮","▲","△"],
    3:["▲","◮","△","▲","◮","△","▲","◮","△"],
    4:["○","✚","⊕","X","□","☒","○","Ξ","㊂"],
    5:["3","1","2","3","2","5","3","2","1"],
    6:["1","2","1","2","3","2","3","4","3"],
    7:["●","○","◎","○","◎","●","◎","●","○"],
    8:["→","↗","↑","↑","↖","←","↖","←","↙"]}
    solutions={
    0:["↘","↙","↖","↗","←","→","↑","↓"],
    1:["●","○","△","▲","■","□"],
    2:["△","◮","▲"],
    3:["△","◮","▲"],
    4:["○","X","㊂","⊕","☒","✚","□","Ξ"],
    5:["1","2","3","4","5","6","7","8","9"],
    6:["1","2","3","4","5","6","7","8","9"],
    7:["●","○","◎"],
    8:["↘","↙","↖","↗","←","→","↑","↓"]}

    number=random.randint(0,len(tests)-1)
    game=tests[number]
    options=solutions[number]
    #put an ? to a random position:
    position=random.randint(0,len(game)-1)
    solution=game.pop(position)
    game.insert(position,"?")
    return game, options, solution


def print_psycho_test(test):
    """Prints the psychotechnical  test as a 3x3 matrix
    -test: It's a list with the test to be printed."""

    for i in range(0,9,1):
        print(test[i],end=" ")
        if (i+1)%3==0:
            print()


def print_psycho_solutions(solutions):
    """Prints all the options for the test
    -solutions: It's a list with all the options of the test
    -Returns a dictionary with the options and a number assigned"""

    options={}
    for i in range (0,len(solutions),1):
        options[i+1]=solutions[i]
        print(f"{i+1}. {options[i+1]}")
    return options


def play_psycho(energy,reputation,day):
    """It's the function for playing the psychotechnical game
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    game,solutions,solution=psycho_test()
    print(f"You have {len(solutions)-1} tries to solve this test\n")

    print_psycho_test(game)
    print()
    options=print_psycho_solutions(solutions)
    tries=len(solutions)
    win=True
    while tries>1:
        guess=check_int_MMCM_in_range("What's the value of '?': ",1,len(options))
        if guess=="mmcm":
            break
        elif options[guess]==solution:
            print("You WIN")
            energy-=1
            break
        print("Wrong Answer")
        tries-=1
        energy-=1
        if tries==len(solutions)//2:
            reputation-=5
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    if tries==1:
        print("You LOSE")
        win=False
        reputation-=10
    energy,day=Input_Output.check_energy(energy,day)
    return energy,reputation,day,win


# play_psycho(20,100,1)
#Hangman ###
def hanged_man(num):
    """Prints the corresponding drawing depending on the state of the hangman game
    -num: It's the number of the position of the drawing"""

    hang_list=["""   |
   |
   |
   |
   |
   |
___|___""","""   _______
   |
   |
   |
   |
   |
   |
___|___""","""   _______
   |     |
   |
   |
   |
   |
   |
___|___""","""   _______
   |     |
   |     ☹
   |      |
   |
   |
   |
___|___""","""   _______
   |     |
   |     ☹
   |     /|\\
   |
   |
   |
___|___""","""   _______
   |     |
   |     ☹
   |     /|\\
   |      /\\
   |
   |
___|___"""]
    print(hang_list[num])


def hangman_word_generator():
    """Generates a word for the hangman minigame from a set
    -REturns the chosen word"""

    words=["detective","victim","crime","sleep","killer","leads",
    "murder","motive","station","solution","clue","tragedy","investigation",
    "disappear","lament","knife","weapon"]

    i=random.randint(0,len(words)-1)
    word=words[i]
    words.remove(words[i])
    word_let=list(word)
    return word_let


def hangman_init_text(word_let):
    """Prints the text required in the hangman minigame as underscores
    -word_let: It's the word going to be guessed in the game"""

    print("You must guess the letters missing: ")
    print("6 tries left")
    for j in word_let:
        print("_",end=" ")
    print("\n\n")


def hangman_play(energy,reputation,day,word_let):
    """It's the function for the hangman minigame
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -word_let: It's the word that is going to be guessed
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
    "Q","R","S","T","U","V","W","X","Y","Z"]

    let_used=[]
    list_guess=[]
    for i in range(0,len(word_let)):
        list_guess.append("_")

    state=-1 #number of the drawing of the hangman
    tries=6
    let_left=len(word_let) #letters left
    win=True
    while True:
        while True:
            x=input("Write your guess: ").strip().lower()
            safe=Input_Output.str_in_list(x,letters)
            safe2=True
            if safe!=True and x!="mmcm":
                print("Invalid guess")
            if len(let_used)!=0:
                for let in let_used:
                    if let==x:
                        safe2=False
                        print("Letter already used\n")
                        break
            if (safe and safe2) or x=="mmcm":
                let_used.append(x)
                break
        if x=="mmcm":
            print("CHEATS MODE ACTIVATED")
            break
        counter=0
        for i in word_let:
            if x==i:
                counter+=1
        let_left-=counter
        energy-=1
        if counter!=0:
            print("Your guess was CORRECT!")
            for k in range(0,len(word_let)):
                if x==word_let[k]:
                    list_guess[k]=x
            for j in range(0,len(list_guess)):
                print(f"{list_guess[j]}",end=" ")
            print()
        else:
            print("Your guess was WRONG!")
            tries-=1
            print(f"{tries} tries left")
            state+=1
            hanged_man(state)
            for j in range(0,len(list_guess)):
                print(f"{list_guess[j]}",end=" ")
            print()
        
        
        
        if let_left==0:
            print("You win! :)")
            break
        if tries==0:
            print("You LOST!")
            reputation-=5
            win=False
            break
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    Input_Output.print_status(energy,reputation)
    return energy,reputation,day,win


# Florecitas-Math figure sequence##
def lit_flw_generator():
    """Generates the value for each flower, and returns a list with each value
    -Returns a list with the value of the rose, the daisy and the orchid"""

    rose=random.randint(1,3)
    daisy=random.randint(1,3)
    orchid=random.randint(1,3)

    return [rose,daisy,orchid]


def little_flowers(fl_list):
    """Generates 3 equations of this format: a_b_c=d.
    - a,b,c are the symbols of the flowers
    - '_' are one operator that can be "x","+","-".
    - d is a number

    -fl_list is the list with the value of each flower (rose, daisy, orchid)"""

    #Taking the values of each flower
    rose=fl_list[0]
    daisy=fl_list[1]
    orchid=fl_list[2]
    operators=["x","+","-"]

    variables=["✿","❀","❁"]
    variables_init={"✿":rose,"❀":daisy,"❁":orchid} #Assigning to each flower theri value

    #Generating each operator
    a1=operators[random.randint(0,2)]
    a2=operators[random.randint(0,2)]
    b1=operators[random.randint(0,2)]
    b2=operators[random.randint(0,2)]
    c1=operators[random.randint(0,2)]
    c2=operators[random.randint(0,2)]

    #Creating the equations
    equation1=[variables[0],a1,variables[random.randint(0,2)],a2,variables[random.randint(0,2)]]
    equation2=[variables[random.randint(0,2)],b1,variables[1],b2,variables[random.randint(0,2)]]
    equation3=[variables[random.randint(0,2)],c1,variables[random.randint(0,2)],c2,variables[2]]

    #Generating the result of the first equation
    if a1==operators[0]: #If the first operator is 'x'
        if a2==operators[0]: #If the second operator is 'x'
            result_eq1=variables_init[equation1[0]]*variables_init[equation1[2]]*variables_init[equation1[4]]
        
        elif a2==operators[1]: #If the second operator is '+'
            result_eq1=variables_init[equation1[0]]*variables_init[equation1[2]]+variables_init[equation1[4]]
        
        elif a2==operators[2]: #If the second operator is '-'
            result_eq1=variables_init[equation1[0]]*variables_init[equation1[2]]-variables_init[equation1[4]]
    
    elif a1==operators[1]: #If the first operator is '+'
        if a2==operators[0]: #If the second operator is 'x'
            result_eq1=variables_init[equation1[0]]+variables_init[equation1[2]]*variables_init[equation1[4]]
      
        elif a2==operators[1]: #If the second operator is '+'
            result_eq1=variables_init[equation1[0]]+variables_init[equation1[2]]+variables_init[equation1[4]]

        elif a2==operators[2]: #If the second operator is '-'
            result_eq1=variables_init[equation1[0]]+variables_init[equation1[2]]-variables_init[equation1[4]]
        
    elif a1==operators[2]: #If the first operator is '-'
        if a2==operators[0]:#If the second operator is 'x'
            result_eq1=variables_init[equation1[0]]-variables_init[equation1[2]]*variables_init[equation1[4]]
        
        elif a2==operators[1]: #If the second operator is '+'
            result_eq1=variables_init[equation1[0]]-variables_init[equation1[2]]+variables_init[equation1[4]]
        
        elif a2==operators[2]: #If the second operator is '-'
            result_eq1=variables_init[equation1[0]]-variables_init[equation1[2]]-variables_init[equation1[4]]
    
    #Generating the result of the second equation
    if b1==operators[0]: #If the first operator is 'x'
        if b2==operators[0]: #If the second operator is 'x'
            result_eq2=variables_init[equation2[0]]*variables_init[equation2[2]]*variables_init[equation2[4]]
            
        elif b2==operators[1]: #If the second operator is '+'
            result_eq2=variables_init[equation2[0]]*variables_init[equation2[2]]+variables_init[equation2[4]]
        
        elif b2==operators[2]: #If the second operator is '-'
            result_eq2=variables_init[equation2[0]]*variables_init[equation2[2]]-variables_init[equation2[4]]
        
    elif b1==operators[1]: #If the first operator is '+'
        if b2==operators[0]: #If the second operator is 'x'
            result_eq2=variables_init[equation2[0]]+variables_init[equation2[2]]*variables_init[equation2[4]]

        elif b2==operators[1]: #If the second operator is '+'
            result_eq2=variables_init[equation2[0]]+variables_init[equation2[2]]+variables_init[equation2[4]]

        elif b2==operators[2]: #If the second operator is '-'
            result_eq2=variables_init[equation2[0]]+variables_init[equation2[2]]-variables_init[equation2[4]]
        
    elif b1==operators[2]: #If the first operator is '-'
        if b2==operators[0]: #If the second operator is 'x'
            result_eq2=variables_init[equation2[0]]-variables_init[equation2[2]]*variables_init[equation2[4]]
        
        elif b2==operators[1]: #If the second operator is '+'
            result_eq2=variables_init[equation2[0]]-variables_init[equation2[2]]+variables_init[equation2[4]]
        
        elif b2==operators[2]: #If the second operator is '-'
            result_eq2=variables_init[equation2[0]]-variables_init[equation2[2]]-variables_init[equation2[4]]
    
    #Generating the result of the third equation
    if c1==operators[0]: #If the first operator is 'x'
        if c2==operators[0]: #If the second operator is 'x'
            result_eq3=variables_init[equation3[0]]*variables_init[equation3[2]]*variables_init[equation3[4]]
    
        elif c2==operators[1]: #If the second operator is '+'
            result_eq3=variables_init[equation3[0]]*variables_init[equation3[2]]+variables_init[equation3[4]]
        
        elif c2==operators[2]: #If the second operator is '-'
            result_eq3=variables_init[equation3[0]]*variables_init[equation3[2]]-variables_init[equation3[4]]
       
    elif c1==operators[1]: #If the first operator is '+'
        if c2==operators[0]: #If the second operator is 'x'
            result_eq3=variables_init[equation3[0]]+variables_init[equation3[2]]*variables_init[equation3[4]]
        
        elif c2==operators[1]: #If the second operator is '+'
            result_eq3=variables_init[equation3[0]]+variables_init[equation3[2]]+variables_init[equation3[4]]
        
        elif c2==operators[2]: #If the second operator is '-'
            result_eq3=variables_init[equation3[0]]+variables_init[equation3[2]]-variables_init[equation3[4]]
        
    elif c1==operators[2]: #If the first operator is '-'
        if c2==operators[0]: #If the second operator is 'x'
            result_eq3=variables_init[equation3[0]]-variables_init[equation3[2]]*variables_init[equation3[4]]
            
        elif c2==operators[1]: #If the second operator is '+'
            result_eq3=variables_init[equation3[0]]-variables_init[equation3[2]]+variables_init[equation3[4]]
        
        elif c2==operators[2]: #If the second operator is '-'
            result_eq3=variables_init[equation3[0]]-variables_init[equation3[2]]-variables_init[equation3[4]]

    #Printing the equations
    print(f"{equation1[0]} {a1} {equation1[2]} {a2} {equation1[4]} = {result_eq1}")
    print(f"{equation2[0]} {b1} {equation2[2]} {b2} {equation2[4]} = {result_eq2}")
    print(f"{equation3[0]} {c1} {equation3[2]} {c2} {equation3[4]} = {result_eq3}")


def ask_flw_value(fl_list):
    """Asks for the values of each flower and returns if you win or not
    -fl_list is the list with the value of each flower (rose,daisy,orchid)"""

    rose=fl_list[0]
    daisy=fl_list[1]
    orchid=fl_list[2]

    r=check_int_MMCM_in_range("Write a integer number between 1 and 3 for the rose ✿: ",1,3)
    if r=="mmcm":
        return True
    d=check_int_MMCM_in_range("Write a integer number between 1 and 3 for the daisy ❀: ",1,3)
    if d=="mmcm":
        return True
    o=check_int_MMCM_in_range("Write a integer number between 1 and 3 for the orchid ❁: ",1,3)
    if o=="mmcm":
        return True
    
    if r==rose and d==daisy and o==orchid:
        print("YOU WIN!")
        return True
    print("YOU LOSE! TRY AGAIN LATER")
    return False


def play_flw(energy,reputation,day):
    """It's the function for playing the flowers
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -murderer: It's the dictionary of the murderer
    -Returns the energy, the reputation, the day and if you win"""

    energy,day=Input_Output.check_energy(energy,day)
    tries=0
    wins=0
    pass_game=True
    print("Find the integer value of the following flowers: ✿  ❀  ❁ (between 1 and 3).\nYou have to win 3 times.\nYou have 10 tries.")
    while tries<10 and wins<3:
        fl_values=lit_flw_generator()
        little_flowers(fl_values)
        win=ask_flw_value(fl_values)
        energy-=1
        if win:
            wins+=1
        else:
            tries+=1
        if tries==5 or tries==10:
            reputation-=tries
        print()
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)

    if tries==10:
        print("YOU LOSE")
        pass_game=False
    return energy,reputation,day,pass_game


# Riddles #######
def quizz_engine(energy,reputation,day):
    """It's the function for the quizz minigame: Prints the riddle-game instructions. It includes all the Riddles and Quizz list (and answers + explanations)
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -murderer: It's the dictionary of the murderer
    -Returns the energy, the reputation, the day and if you win"""
    
    energy,day=Input_Output.check_energy(energy,day)
    print("\n********* THE QUIZZ GAME *********\n\nYou must correctly answer the 3 questions that I will propose to you...\nif you are not able to do so, you lost.\n")
 
    quizz_set=["Only 12 set foot on that place, he was the last to leave, and more than 50 years have to pass until someone goes there to live... Who is he?",
    "A hundred years ago they may have reached the Sagarmatha before anyone else. But they did not live to tell the tale",
    "After an epic adventure like no other one, he returned to rescue his crew at a place called <<elephant>>",
    "Johannes Kepler deduced his 3 laws based on visual observations (before the invention of the telescope) of a great astronomer, who?",
    "Albert Einstein managed to publish in 1905 the articles on the Photoelectric Effect, the Brownian Movement and the Special Theory of Relativity thanks to the collaboration of a great scientist, who?",
    "What is a large cloud of gas and dust in interstellar space, a region in Space where stars are born",
    "What object in the solar system is considered a dwarf planet?",
    "A ship is anchored in the port. On one of its sides a staircase descends, whose steps are separated from each other by 30cm. The ladder is submerged to the keel. The tenth step from the deck is flush with the water. The tide falls 2.1m... Which step will now be aligned with the water?",
    "Which of these is a major concern about the overuse of antibiotics?",
    "A car travels at a constant speed of 40 miles per hour. How far does the car travel in 45 minutes?",
    "How many bones are in the human body?","How many states of matter are there?",
    "At what temperature are Celsius and Fahrenheit equal?",
    "What metal is the best conductor of electricity?"]
 
    quizzset_answers=[
    ["a    Eugene Cernan","b    Edmund Hillary", "c    Roald Amundsen", "d    Robert Falcon Scott"],
    ["a    Robert Peary and Robert Bartlett","b    George Mallory and Andrew Irvine","c    Hernán Cortés and Francisco Pizarro","d    James Glaisher and Henry Coxwell"],
    ["a    Ulises of Ithaca","b    Harrison Odjegba Okene","c    Juan Figaredo Pidal","d    Ernest Shackelton"],
    ["a    Tycho Brahe","b    Nicholas Copernicus","c    Diego Pérez de Mesa","d    Philip Melanchthon"],
    ["a    Niels Bohr","b    Bernhand Riemann","c    Mileva Maric","d    Max Plank"],
    ["a    Protostar","b    Galaxy","c    Nebula","d    Black hole"],
    ["a    Ceres","b    Ganymede","c    Pluto","d    a and c are correct"],
    ["a    10th","b    17th","c    21th","d    15th"],
    ["a    It can lead to antibiotic-resistant-bacteria","b    There will be an antibiotic shortage","c    Antibiotics will get into the water system","d    Antibiotics can cause secondary infections"],
    ["a    25 miles","b    30 miles","c    35 miles","d    40 miles"],
    ["a    402","b    110","c    260","d    206"],
    ["a    4","b    3","c    5","d    6"],
    ["a    100º","b    -40º","c    12º","d    -12º"],
    ["a    cooper","b    gold","c    iron","d    silver"]]
 
    quizzset_explanations=["Eugene Cernan left the Moon on December 14, 1972 after landing three days earlier on the Apollo XVII mission.",
    "George Mallory and Andrew Irvine lost their lives on their 1924 expedition to Everest (Sagarmatha). Some people believe they were the first to reach the summit, but died on the way down.",
    "On August 30, 1915, after an epic journey, Shackleton returned to Elephant Island aboard a Chilean tug to pick up the rest of the crew and return safely to England. The Endurance in the distance, trapped by polar ice.",
    "Tycho Brahe was a Danish astronomer, considered the greatest observer of the sky in the period before the invention of the telescope. Before his death he signed over his records to Johannes Kepler.",
    "Mileva Maric was the first wife of Alfred Einstein. It is believed that the data from the 6 months of 1887 in which she studied with Philipp Lenard in Heidelberg, Germany on the theory of heat and electrodynamics were fundamental in the later study of the photoelectric effect by the Einstein couple. ",
    "nebulae are the stars' nurseries","On August 24, 2006, the International Astronomical Union, disregarding the weight of history, demoted Pluto to the status of a dwarf planet, a category that also includes Ceres, previously considered a huge asteroid.",
    "As long as the load on board does not change, a ship floats on the water without changing its position relative to the surface.","The bacteria resistance to antibiotics is becoming a serious risk to human health.",
    "At that speed the car travels 40 miles in an hour. In three quarters of an hour the vehicle will cover three quarters of that distance (30 miles).","There are just 206 bones in our body","4: solid, liquid, gas and plasma","-40ºC = -40ºF",
    "Silver: considered the best conductor of electricity, although due to its high cost it is usually used in specific cases"]

    correct_answer=["a","b","d","a","c","c","d","a","a","b","d","a","b","d"]
 
    
    streak=0 #questions win
    win=True
    while True:
        question=quizz_set[random.randint(0,len(quizz_set)-1)]
        print(question)
        for i in range(0,len(quizz_set)):
            if question==quizz_set[i]:
                num=i
                print(quizzset_answers[i][0])
                print(quizzset_answers[i][1])
                print(quizzset_answers[i][2])
                print(quizzset_answers[i][3])
        while True:
            answer1=input("What do you choose (from a to d): ").strip()
            
            answer=answer1.lower()
            if answer!="a" and answer!="b" and answer!="c" and answer!="d" and answer!="mmcm":
                print ("invalid answer")
            else:
                break
        if answer=="mmcm":
            print("CHEATS MODE ACTIVATED")
            break
        energy-=1
        
        if answer==correct_answer[num]:
            print("Correct answer!")
            streak+=1
            if streak==3:
                print()
                print("YOU WIN!")
                break
 
            quizz_set.pop(num)
            quizzset_answers.pop(num)
            quizzset_explanations.pop(num)
            correct_answer.pop(num)
 
        else:
            print("YOU HAVE LOST!")
            print(f"Explanation: {quizzset_explanations[num]}")
            print()
            
            win=False
            reputation-=5
            Input_Output.print_status(energy,reputation)
            break
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    return energy,reputation,day,win


# Cards game ######
def highest_card_instructions():
    """Instructions for the game Draw the Card
    -Returns the type of figures and number of figures"""

    print("\n**********DRAW THE CARD**********\n")
 
    type_of_figures=["♠", "♣", "♥", "♦"]
    number_of_figures=["ACE","2","3","4","5","6","7","8","9","10","J","Q","K"]
    #Creating the deck
    for j in range(0,len(number_of_figures)):
        if j!=9 and j!=10 and j!=11 and j!=12 and j!=0:
            print(f"♠{j+1}    ♣{j+1}    ♥{j+1}    ♦{j+1}" )
        elif j==0:
            print(f"♠ACE  ♣ACE  ♥ACE  ♦ACE" )
        elif j==10:
            print(f"♠J    ♣J    ♥J    ♦J" )
        elif j==11:
            print(f"♠Q    ♣Q    ♥Q    ♦Q" )
        elif j==12:
            print(f"♠K    ♣K    ♥K    ♦K" )
        elif j==9:
            print(f"♠{j+1}   ♣{j+1}   ♥{j+1}   ♦{j+1}" )
 
    print("""\nThat deck of cards has been shuffled and a random card has appeared.
You will have to choose if the next card will be higher or lower than the current one. If the next card that comes out matches your choice, you
can play again, then the card comes back to the deck and it will be shuffled again before another random card will appear.
If you guess correctly 3 times in a row you will win the game, and whenever you reach 10 tries, the game will end.""")
    return type_of_figures,number_of_figures


def highest_card_engine(type_of_figures,number_of_figures):
    """It's the game_engine
    -type_of_figures: It's a list with all the types of figures
    -number_of_figures: It's a list with all the numbers of the cards
    -Returns if you win or not"""
    
    tries=0
    initial_card=[type_of_figures[random.randint(0,3)],number_of_figures[random.randint(0,12)]]
    while True:
        for r in range (2,15):
            if initial_card[1]==str(r):
                initial_card_value=r
                #print(f"Valor de carta inicial: {initial_card_value}")
            elif initial_card[1]=="ACE":
                initial_card_value=14
            elif initial_card[1]=="J":
                initial_card_value=11
            elif initial_card[1]=="Q":
                initial_card_value=12
            elif initial_card[1]=="K":
                initial_card_value=13
 
        print(f"\nCurrent card: {initial_card[0]}{initial_card[1]}\nWHAT DO YOU THINK ABOUT THE NEXT CARD?")
 
        while True:
            answer=input("IS IT HIGHER (H) OR LOWER (L)? ").strip().lower()
            if answer!="h" and answer!="l" and answer!="mmcm":
                print ("Invalid answer")
            else:
                break
        
        if answer=="mmcm":
                print("CHEATS MODE ACTIVATED")
                return True
        
        while True:
            next_card=[type_of_figures[random.randint(0,3)],number_of_figures[random.randint(0,12)]]
            if next_card[0]==initial_card[0] and next_card[1]==initial_card[1]:
                continue
            else:
                break
 
        for s in range (2,15):
            if next_card[1]==str(s):
                next_card_value=s
            elif next_card[1]=="ACE":
                next_card_value=14
            elif next_card[1]=="J":
                next_card_value=11
            elif next_card[1]=="Q":
                next_card_value=12
            elif next_card[1]=="K":
                next_card_value=13

        print(f"\nThe next card is: {next_card[0]}{next_card[1]}")
        if answer=="h" and next_card_value>=initial_card_value or answer=="l" and next_card_value<=initial_card_value:
            print("YOU WON THIS ROUND!\n")
            tries=tries+1
            initial_card=next_card
            if tries==3:
                print("3 CORRECT GUESSES IN ROW: YOU WON!")
                return True
        else:
            print("YOU LOST")
            return False


def play_cards(energy,reputation,day):
    """It's the function for playing the cards minigame
    -energy: It's the energy of the detective
    -reputation: It's the reputation of the detective
    -day: It's the days passed
    -murderer: It's the dictionary of the murderer
    -Returns the energy, the reputation, the day and if you win"""
    
    energy,day=Input_Output.check_energy(energy,day)
    tries=0
    win=False
    type_of_figures,number_of_figures=highest_card_instructions()

    while tries<10 and not win:
        win=highest_card_engine(type_of_figures,number_of_figures)
        if not win:
            tries+=1
        energy-=1
        if tries==5:
            reputation-=5
        energy,day=Input_Output.check_energy(energy,day)
        Input_Output.print_status(energy,reputation)
    
    if tries==10:
        print("YOU HAVE LOST")
    return energy,reputation,day,win 


#play_cards(20,100,1)
# Trial #########################################
#FOUR SUSPECTS->One function depending on who you chose to take to the trial
#Therefore, you HAVE to chose who is your suspect
#And it will change whether the person is innocent or not
#And thus, we have to choose who is our suspect
###############################################################################
#OTHER TRIAL STUFF
def expose_murderer(dect_name,mySus,murderer,per_points):
    """Plays the different paths in which a suspect is accused, depending if
    the player got the murderer, motive and weapon right or wrong
    -detc_name: It's the name of the detective
    -mySus: It's the name of the suspect
    -murderer: It's the dictionary with all the information of the murderer
    -per_points: They are they performance points
    -Returns the performance points and the suspect"""

    while True:
        weapon,motive=ask_for_proof(dect_name,mySus) #goes to the function ask_for_proof to get the weapon and the motive

        if weapon==murderer["weapon"] and motive==murderer["motive"] and mySus==murderer["name"]: #EVERYTHING IS CORRECT -> murderer, weapon and suspect prints the exposition text and the final text, and breaks the loop
            if mySus=="Matthew":
                characters.m_expose_txt(dect_name,motive)
                characters.m_final(mySus)
                break
            elif mySus=="Veronica":
                characters.v_expose_txt(dect_name,motive)
                characters.v_final(mySus)
                break
            elif mySus=="Bob":
                characters.b_expose_txt(dect_name,motive)
                characters.b_final(mySus)
                break
            elif mySus=="Lilian":
                characters.l_expose_txt(dect_name,motive)
                characters.l_final(mySus)
                break
        
        elif mySus==murderer["name"]: #WEAPON AND/OR MOTIVE IS WRONG -> goes to the function for the text when something is wrong
            bad_proof(dect_name,mySus,weapon,motive)
            print("\nJudge: Indeed... I think you did")
            print(f"{dect_name}: Did I mess up again?\n")
            minus=5
            per_points=low_points(per_points,minus) #lowers the performance points accordingly
            print(f"YOUR PERFORMANCE POINTS HAVE BEEN LOWERED BY {minus}, INTRODUCE YOUR PROOF AGAIN")
            #loop starts again
        
        else: #MURDERER IS WRONG -> goes to the function for the text when something is wrong
            bad_proof(dect_name,mySus,weapon,motive)
            print("Judge: Indeed... I think you did")
            print("Judge: Are you sure we have the right suspect here?")
            print(f"{dect_name}: Did I mess up again?\n")
            minus=10
            per_points=low_points(per_points,minus) #lowers the performance points accordingly
            print(f"YOUR PERFORMANCE POINTS HAVE BEEN LOWERED BY {minus}, INTRODUCE YOUR SUSPECT AGAIN.")
            print()
            mySus=ask_for_sus(dect_name) #asks for the suspect again
            characters.mySus_txt_init(mySus) #prints the initial text for the new suspect again (m_init_txt...)
            #loop starts again
    return per_points,mySus


def bad_proof(dect_name,mySus,weapon,motive):
    """Prints what needs to be seen in case the player got the motive and/or
    weapon wrong
    -dect_name: It's the name of the detective
    -mySus: It's the name of the suspect
    -weapon: It's the weapon of the suspect
    -motive: It's the motive of the suspect"""

    #is used in case the player has something wrong (murderer or weapon and/or motive)
    weapon_list={"Pushed":"being pushed and hit her head",
    "Knife":"being stabbed by a knife",
    "Strangled":"being strangled suddenly",
    "Poison":"being poisoned and falling in the pool once she lost consciousness"}

    print(f"""
{dect_name}: {mySus}'s motive was simple, {motive.lower()}. As for the weapon, it can be clearly seen that she died because of {weapon_list[weapon]}.\n
Did I make any mistake?""")


##################
#PROOF AND SUS STUFF
def ask_for_sus(dect_name):
    """Asks the player to introduce their suspect
    -dect_name: It's the name of the detective
    -Returns the name of the suspect capitalized"""

    #ASK FOR THE CULPRIT
    while True:
        print()
        sus_chosen=input(f"""\nJudge: {dect_name}, who do you think is the murderer?:
    - Matthew
    - Bob
    - Veronica
    - Lilian
""").strip().lower()

        if (sus_chosen!="veronica" and sus_chosen!="bob" and
        sus_chosen!="matthew" and sus_chosen!="lilian"): #ensures the option selected is correct ignoring the case
            print(f"{dect_name}: Wait, who is that anyways?")

        else:
            mySus=sus_chosen.capitalize()
            break
    print(f"\n{mySus} is asked to declare in front of the court")
    return mySus


def ask_for_proof(dect_name,mySus):
    """Asks the player for how the victim was killed and the motive of their
    suspect
    -dect_name: It's the name of the detective
    -mySus: It's the name of the suspect
    -Returns the weapon and motive selected"""

    while True:
        weapon=input(f"""\nJudge: {dect_name}, how did {mySus} murder the Madame:
    - Pushed
    - Knife
    - Strangled
    - Poison\n""").strip().lower().capitalize()
        if weapon!="Knife" and weapon!="Strangled" and weapon!="Pushed" and weapon!="Poison": #ensures the option selected is correct ignoring the case
            print(f"{dect_name}: No... that doesn't make any sense! Gotta focus")
        else:
            break

    while True:
        motive=input(f"""\nJudge: Well... and why did {mySus} killed her:
    - Heartbreak
    - Jealousy
    - Vengeance
    - Money\n""").strip().lower().capitalize()

        if motive!="Heartbreak" and motive!="Jealousy" and motive!="Vengeance" and motive!="Money": #ensures the option selected is correct ignoring the case
            print(f"{dect_name}: No... that doesn't make any sense! Gotta focus")
        else:
            break

    print("\n\n")
    return weapon,motive


################################################################################
#GAME
def trial_g_init():
    """Prints the instructions of the trial minigame"""

    print("""\n\n\n You are almost finished, congratulations!
For this game, your lucky number will be provided at the beginning. You'll draw a two dice, and if you get your lucky number you'll win, if you
get an even number you will do a strong attack, and if you get an odd one you will do a weak attack. Your opponent's argument will take two of 
your hp per round. To win, you have to defeat every argument.\n\tGood luck!\n""")


def trial_game(dect_name,mySus):
    """Initiates the trial minigame
    -dect_name: It's the name of the detective
    -mySus: It's the name of the suspect
    -Returns if you win or lose"""

    trial_g_init() # prints the initial text for the minigame (the instructions)
    input("Press Enter to begin the final battle against your opponents arguments!\n")

    #Counterpoins
    #MATTHEW (What he says)
    m_counterpoints=["How could I even do that? She was my mother!",
    "I never knew she had a diary",
    "Aren't her and my uncle the criminals here?!"]
    #what you respond with - dictionaries (good for best attack, b1 for the 2nd best, b2 for the worst answer):
    m_attaks1={"good":"There's proof that you did.","b1":"Don't try to act innocent!","b2":"Well, did you even care?"}
    m_attaks2={"good":"Your fingerprints all over it say otherwise.","b2":"Don't play dumb!","b1":"Your reactions through the session are suspicious."}
    m_attaks3={"good":"Yes, but that doesn't mean that you aren't as well.","b1":"This was the wrong way to prove it","b2":"It seems you're one too."}

    #VERONICA (What she says)
    v_counterpoints=["This whole accusation is utterly ridiculous!",
    "How did you find out about my husband anyway? I'll sue you for violating our privacy!",
    "Did you even find the kitchen knife?"]

    v_attaks1={"b2":"You're right, let's leave (sarcasm).","b1":"Says the one who's knife has been found","good":"The court will be the judge to that."}
    v_attaks2={"b2":"Are you serious lady?","b1":"Will you be able to do that from jail?","good":"It was justified as it was crucial for the investigation."}
    v_attaks3={"b2":"Are you SERIOUS lady?","b1":"Yeah, it was found, but who mentioned it was such a knife?","good":"You've exposed yourself, who said it was a kitchen knife?"}

    #BOB (What he says)
    b_counterpoints=["I would never do that to my brother! We were family!",
    "There's no actual proof of the affair, is there? We did not have that kind of relationship",
    "I loved her, I didn't kill her!"]

        #b_attacks1 good needs the computer stuff to be about the affair in his case
    b_attaks1={"b2":"Do you really think now is the time to play the 'family' card?","good":"Madame's diary says otherwise","b1":"That fact doesn't mean you didn't do it, you were his wife's affair partner after all."}
    b_attaks2={"b2":"It sure is... ... look at the report!","good":"There's her diary, which should be more than enough.","b1":"Her cats are suspiciously close to you, right?"}
    b_attaks3={"b1":"Even if you did love her, that doesn't change the outcome.","good":"There's plenty of proof against you.",
    "b2":"There's one step from love to hate."}

    #LILIAN (What she says)
    l_counterpoitns=["How can you prove that I knew where the money was?",
    "You can't really build a case with such proofs",
    "I would never betray her like that! She trusted me!"]

    l_attaks1={"b2":"How can you prove you didn't know?","good":"Well, a hair was found and there's none other red-haired person around, hm?",
    "b1":"A housekeeper that was like a confidant and a servant should know more than they let be seen, right?"}
    l_attaks2={"b2":"Care to reason why?","good":"Proof is proof no matter how meaningless it may seem.","b1":"Plenty of cases have been resolved with even less."}
    l_attaks3={"b2":"Yet you did...","good":"That subjective judgment will not deny the proof.","b1":"Trusting you was a fatal mistake then."}

    #dictionary with the symbols for the dices (depending on what you get it'll use the corresponding one)
    dices={1:"⚀",2:"⚁",3:"⚂",4:"⚃",5:"⚄",6:"⚅",7:"⚀⚅",8:"⚃⚃",9:"⚃⚄",10:"⚄⚄",11:"⚅⚄",12:"⚅⚅"}

    hp_list=[20,30,40] #The amount of life of the arguments (m_counterpoints for example) in order (1st one->20, 2nd->30...)
    att_list=[[5,3],[8,5],[12,8]] #The damage of your attacks (for 1st argument, the worst response deals 3 dmg and the second worst 5). The best attack is not defined because it is the same hp as the one the argument you're again has

    my_hp=30 #player's hp, 2 points will be lowered each time the loop is repeated unless they 'kill' the argument

    for i in range(0,len(hp_list)): #a for loop for the three arguments launched
        hp=hp_list[i] #selects the hp of the argument depending on the value of i
        #several ifs to select the argument you are against (m_counterpoints) and your answers (m_attacks...)
        if mySus=="Matthew":
            who_against=m_counterpoints
            if i==0:
                my_comebacks=m_attaks1
            elif i==1:
                my_comebacks=m_attaks2
            elif i==2:
                my_comebacks=m_attaks3
        elif mySus=="Veronica":
            who_against=v_counterpoints
            if i==0:
                my_comebacks=v_attaks1
            elif i==1:
                my_comebacks=v_attaks2
            elif i==2:
                my_comebacks=v_attaks3
        elif mySus=="Bob":
            who_against=b_counterpoints
            if i==0:
                my_comebacks=b_attaks1
            elif i==1:
                my_comebacks=b_attaks2
            elif i==2:
                my_comebacks=b_attaks3
        elif mySus=="Lilian":
            who_against=l_counterpoitns
            if i==0:
                my_comebacks=l_attaks1
            elif i==1:
                my_comebacks=l_attaks2
            elif i==2:
                my_comebacks=l_attaks3

        g_or_b=["good","b1","b2"] #a list with the dictionaries index
        #selects the items from the dictionary (your answers) by poping the indexes from the list so that they will always be printed in the same order and not repeated
        choice1=my_comebacks[g_or_b.pop(random.randint(0,len(g_or_b)-1))]
        choice2=my_comebacks[g_or_b.pop(random.randint(0,len(g_or_b)-1))]
        choice3=my_comebacks[g_or_b.pop(0)]
        
        # GAME LOOP #######
        while True:
            print(f"""\n{"♡"*hp} : {hp} HP
{mySus}: {who_against[i].upper()}\n""") #prints the same amount of hearts as the hp the argument has, the number of hp, and the enemy saying the argument

            print(f"""\nQUICK! How do we counter this?
    - {choice1}
    - {choice2}
    - {choice3}\n
THROW THE DICE!\n""")

            lucky_num=random.randint(1,12) #selects your lucky number for this round randomly
            print(f"Your lucky number for this round is {lucky_num}{dices[lucky_num]}...") #prints that number
            dice=random.randint(1,12) #selects the number you draw from the dice

            while True:
                att=input("SAY 'CONFESS' TO ATTACK!: ").strip().lower() #asks the player to input 'confess' to throw the attack
                print(att)
                print(att=="confess")
                if att!="confess": #launched in case you input something different from confess
                    print(f"\n{dect_name}: THIS IS NOT THE TIME FOR THIS!!!!!")
                else:
                    break

            print(f"... and you have drawn a {dice}{dices[dice]}!") #prints what you've drawn
            if lucky_num==dice: #in case you draw the same as the lucky number
                hp-=hp_list[i] #the arguments hp is lowered by the value of its initial hp
                print(f"\n- {dect_name}: ",end="")
                print(my_comebacks["good"].upper()) #prints your comeback
                

            elif dice%2==0:
                hp-=att_list[i][0]
                print(f"\n- {dect_name}: ",end="")
                print(my_comebacks["b1"].upper()) #prints your comeback
                if hp>0:
                    my_hp-=2
                
            elif dice%2==1:
                hp-=att_list[i][1]
                print(f"- {dect_name}: ",end="")
                print(my_comebacks["b2"].upper())
                if hp>0:
                    my_hp-=2
       
            print(f"\nYour remaining hp is ♡ : {my_hp} HP\n") #prints your remaining hp

            if hp<=0:
                print("YOU HAVE DEFEATED THIS ARGUMENT!") #printed in case you defeat the current argument
                break
            else: #in case you don't defeat it, prints the remaining hp of the argument
                print(f"There's {hp} points of remaining HP.")
                print(f"{dect_name}: Seems this was not my brightest comeback.\n")
            if my_hp==0: #prints in case you lose all your hp, stopping the game and returning false (not win)
                print("YOU'VE LOST! ☹")
                return False
    print("YOU'VE WON! ㋡")
    return True #returns true in case you win


def low_points(per_points,minus):
    """Lowers the performance points by the quantity provided
    -per_points: They are they performance points
    -minus: Subsracts that quantity from the performance points
    -Returns the per_points after substracting"""

    per_points-=minus
    return per_points


################################################################################
#THE ACTUAL TRIAL
def trial_init_txt():
    """Prints the text needed before starting the trial minigame"""

    print("""\n

████████ ██████  ██  █████  ██      
   ██    ██   ██ ██ ██   ██ ██      
   ██    ██████  ██ ███████ ██      
   ██    ██   ██ ██ ██   ██ ███████       
                                    \n""")
    print("The day for the murderer to be uncovered has arrived \nA show where truth and lies intertwined, ready to be exposed \nTime to bring justice to this case!")


def trial_ending(dect_name,mySus):
    """Prints the ending of the trial
    -dect_name: It's the name of the detective
    -mySus: It's the name of the suspect"""


    print("""\n
╔╦╗┬─┐┬┌─┐┬    ┌─┐┌┐┌┌┬┐┌─┐
 ║ ├┬┘│├─┤│    ├┤ │││ ││└─┐
 ╩ ┴└─┴┴ ┴┴─┘  └─┘┘└┘─┴┘└─┘""")
    print(f"""
    The session comes to an end, at last...
    You have been able to expose the truth about Madame's case after everything that has happened.
    {mySus} has been sentenced to a pretty long sentence, 35 years is not laughing matter.
    Justice was served, right?\n
    ...\n
    {dect_name}, leaving: Well, I guess I can treat myself to a nice dinner tonight. After all, I'll keep my job, right?\n
    LET'S SEE!\n""")


def main_trial(dect_name,murderer):
    """Plays the whole trial
    -dect_name: It's the name of the detective
    -murderer: It's the dictionary with all the information of the murderer
    -Returns the performance points"""

    #BEGINNING TEXT AND QUESTIONS
    per_points=100 #initial value of the trial's performance points, which will be lowered by the player's mistakes/loses across it
    trial_init_txt() #prints the initial trial text
    print(f"This are your starting performance points, each mistake will lower them: {per_points}") #prints your initial performance points


    mySus=ask_for_sus(dect_name) # Asks you for your suspect and returns it
    characters.mySus_txt_init(mySus) # Prints the initial text for your suspect
    per_points,mySus=expose_murderer(dect_name,mySus,murderer,per_points) # Exposes the murderer, after asking for proof and ensuring everything is correct,
    # Returning the performance points and the suspect (in case it was wrong at first)


    print(f"This are your current performance points: {per_points}. If you lose the game they will be lowered.")

    #THE ACTUAL GAME BEGINS
    while True:
        game=trial_game(dect_name,mySus) # Calls the game function (that also contains the instructions)
        if not game: #YOU LOST
            print()
            minus=25
            per_points=low_points(per_points,minus)
            print(f"YOUR PERFORMANCE POINTS HAVE BEEN LOWERED BY {minus}, TRY AGAIN")
            #repeats the loop
        
        else: #YOU WON
            break
    
    trial_ending(dect_name,mySus) #calls the function with the final text for the trial
    return per_points


################################################################################
# dect_name=ask_player_name()
# murderer=characters.sus_selection()
# print(murderer) #para ver que tira
# per_points=main_trial(dect_name,murderer)
# print(per_points)
#per_points son los perfomance points
#AQUÍ USARÍAMOS UNA FILE PARA CALCULAR EL SCORE QUE SERÍA LO QUE RETORNARÍA LA
#FUNCIÓN SCORE, QUE DEBERÍA TENER COMO PARÁMETROS PER_POINTS,REPUTATION Y TIME
#—-------------------------------------------------------------------------------