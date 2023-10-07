import random
matthew={"name":"Matthew", "age":20, "gender":"male", "surname":"Evans",
"weapon":"Pushed", "motive":"Vengeance", "library":"a little diamond of a very expensive watch. I think Matthew have one during the interrogation", "living": "a prepared talk for Madame very disorganized with cross out words, saying that he knows her secret.",
"son's":"If you ever have any trouble with your mother, just come and tell me, ok?-Love you, Dad",
"kitchen":"an expensive handkerchief with mud in the trash can, this person tried to clean the footprints of the floor. It has an 'M' embroidered",
"bedroom":"Matthew is more distant, he tried talking to me but he was speechless. I think he knows something..."} #madame writes the entries

lilian={"name":"Lilian", "age":62, "gender":"female", "surname":"Adams",
"weapon":"Poison", "motive":"Money", "library":"a red hair","living":"a list with some groceries to buy. At the end underlined: PHARMACY before the party.",
"son's":"I think Lilian likes so much the riches's lifestyle",
"kitchen":"a lot of strange drinks are in the trashcan, also there are some drugs",
"bedroom":"Lilian has been giving me a dirty look at my back for some months. I don't know why now it's like this"}

bob={"name":"Bob", "age":63, "gender":"male", "surname":"Evans",
"weapon":"Strangled", "motive":"Heartbreak", "library":"a ring with two letters 'B' and 'M'", "living":"a love poem. It has a B and it' says that he was her real love.",
"son's":"Bob is not to be trusted, he looks at your mother strangely.",
"kitchen":"a napkin with blood is in the trash. Bob had an injury during the interrogation",
"bedroom":"Bob has been very annoying asking me out all the time. I am over it, it was just a favour"}

veronica={"name":"Veronica", "age":54, "gender":"female", "surname":"Smith",
"weapon":"Knife", "motive":"Jealousy", "library":"an acrylic nail","living":"a check with the signature of Veronica. It's only missing Madame's signature.",
"son's":"Veronica is a very envious woman",
"kitchen":"in one cupboard a knife is missing, and it has some sequins and purpurin",
"bedroom":"I don't feel bad for Veronica being a poor person now. She thinks I don’t know but whatever. She has been asking me money subtly lately"}

suspects={"Veronica":veronica,"Lilian":lilian,"Matthew":matthew,"Bob":bob}

def sus_selection(suspects):
    """At the beginning of the game, selects the culprit randomly and returns all its information
    -suspects: It's a dictionary with all the suspects and their information"""

    names=["Matthew","Lilian","Veronica","Bob"]
    return suspects[names[random.randint(0,len(names)-1)]] #selects and returns one dictionary randomly


def return_clue(murderer,suspects,clue):
    """Returns a wrong clue
    -murderer: It's the murderer of the case
    -suspects: It's a dictionary with all the suspects and their information
    -clue: It's the name of the clue"""

    names=["Veronica","Lilian","Matthew","Bob"]
    names.remove(murderer["name"])
    name=names[random.randint(0,len(names)-1)]
    return suspects[name][clue]


# TRIAL STUFF TEXT CHARACTERS ######
def mySus_txt_init(mySus):
    """Prints the initial text for the suspect selected
    -mySus:It's the name of the suspect selected"""

    if mySus=="Matthew":
        m_init_txt()
    elif mySus=="Veronica":
        v_init_txt()
    elif mySus=="Bob":
        b_init_txt()
    elif mySus=="Lilian":
        l_init_txt()


##################
# MATTHEW STUFF
def m_init_txt():
    """Prints the initial text of Matthew's path"""

    print("\tWithout saying a word, Matthew takes a seat. \nHe looks at you with his wide, death blue eyes...\n")
    print(f"Judge: What do we have here? Matthew Evans, the son of the victim, \n who is just 20 years old...\n")


def m_expose_txt(dect_name,motive):
    """Prints the text the player says exposing the truth in Matthew's path in the trial when he is the killer
    -dect_name: It's the name of the detective
    -motive: It's the motive of the crime if it was Matthew"""

    print(f"""
    {dect_name}: Matthew's motive was {motive.lower()}, as he discovered the truth behind her mother and uncle's affair and the death of his father. My honor, the
victim was fond of him, and his death was registered as a car accident caused by his own negligence. But he recently discovered in her mother's diary
that it all was truly caused by a sabotage, which was caused by none other that the deceased's brother, and instigated by her.\n
    When he went to confront his mother about it, she didn't deny it, am I wrong?\n
    *Matthew stays silent*\n
    His mother covered Bob in order for her to still get the inheritance, given that the affair would be uncovered otherwise, leaving her out of it by 
the clauses witten by the father.\n
    Matthew was quickly to catch up on that, and, utterly infuriated, pushed her to the pool, only to realize later on that this caused her to hit her
head and die.""")


def m_final(mySus):
    """Prints the final sentence Matthew says before starting the minigame
    -mySus:It's the name of the suspect selected"""

    print(f"""\nDid I make any mistake?\n
{mySus}'s Lawyer:...\n
Matthew: This...\nTHIS WON'T BE THE END!\n""")


##################
# VERONICA STUFF
def v_init_txt():
    """Prints the initial text of Veronica's path"""

    print("""\tDramatically, Veronica takes a seat while accusing everyone of being against her.\nShe takes at glance at you before continue blabbing\n""")
    print(f"""\nJudge: What do we have here? Veronica Smith, the best friend of the victim...\n""")


def v_expose_txt(dect_name,motive):
    """Prints the text the player says exposing the truth in Veronica's path in the trial when she is the killer
    -dect_name: It's the name of the detective
    -motive: It's the motive of the crime if it was Veronica"""

    print(f"""\n
    {dect_name}: Veronica's motive was {motive.lower()}. For her, seeing her best friend continuing having the same lifestyle they always enjoyed while she was 
struggling to keep up appearances, was horrible.\n
    You see my honor, upon further investigation, it was discovered that her husband was recently forced to take up on early retirement due to internal
matters. Due to their excessive expendings, they did not have that much money saved up, but their dignity pushed Veronica to keep her mouth shut about
everything.\n
    But seeing the victim throwing such gatherings and parties...It finally got to her nerves.\n
    *Veronica was about to complain when her lawyer told her to keep it to herself*\n
    But, she decided that ending her was not that great of a plan, so she thought that her best friend of years could her help, right? She told her 
everything she was going through, all her struggles, all for Madame to deny any help and, who knows? Maybe she even laughed.\n
    *Veronica looks away*\n
    That's why she stabbed her multiple times. One after another. How could she do this to her, right? \n
    """)


def v_final(mySus):
    """Prints the final sentence Veronica says before starting the minigame
    -mySus:It's the name of the suspect selected"""

    print(f"""\nDid I make any mistake?\n
{mySus}'s Lawyer:...\n
Veronica: I...\nI WON'T GO DOWN LIKE THIS!\n""")


##################
#BOB STUFF
def b_init_txt():
    """Prints the initial text of Bob's path"""

    print("Walking arrogantly, Bob proceeds to take a seat\nHe looks at you with a sense of superiority\n\n")
    print("Judge: What do we have here? Bob Evans, the ex-brother in law of the victim...\n""")


def b_expose_txt(dect_name,motive):
    """Prints the text the player says exposing the truth in Bob's path in the trial when he is the killer
    -dect_name: It's the name of the detective
    -motive: It's the motive of the crime if it was Bob"""

    print(f"""\n
{dect_name}: Bob's motive was {motive.lower()}. He was the boyfriend of the victim a long while before she even got to know his brother, who would end up marrying her.\n
    When Madame discovered that the fortune of his brother was greater than his, she decided that Bob was no longer good enough. Taking advantage
of the fact that she hadn't being introduce to him yet, she broke up with Bob out of no where, only for him to realize months later that she was
know with his brother.\n
    *Bob doesn't seem faced by these words*\n
    Bob was truly about to tell him the truth about Madame when she approached him, seducing him once again in what would become their affair. Only
for him to fall in her trap when she convinced him to sabotage his brother's car, promising to share the money.\n
Bob: Agh...\n
    And when she took of with almost everything, he realized he was fooled, so he decided that, after such a heartbreak, dirtying his hands again
wouldn't be that bad...\n
    All of his interactions with her from then on where a plan to get close again and finally end with the one that played with him and his heart over
and over again.\n""")


def b_final(mySus):
    """Prints the final sentence Bob says before starting the minigame
    -mySus:It's the name of the suspect selected"""

    print(f"""\n\nDid I make any mistake?\n
{mySus}'s Lawyer:...\n
Bob: I'LL PROVE YOUR WRONGDOINGS!\n""")


##################
#LILIAN STUFF
def l_init_txt():
    """Prints the initial text of Lilian's path"""

    print("As calm as ever, Lilian walks to her seat \nHowever, she gives you a deathly look\n")
    print(f"""\nJudge: What do we have here? Lilian Adams, the housekeeper of the victim...\n""")


def l_expose_txt(dect_name,motive):
    """Prints the text the player says exposing the truth in Lilian's path in the trial when she is the killer
    -dect_name: It's the name of the detective
    -motive: It's the motive of the crime if it was Lilian"""

    print(f"""\n
{dect_name}: Lilian's motive was {motive.lower()}. She was not only the most trusted and loyal servant of the victim, but one of her closest confidants. Whenever
the Madame was frustrated with something, burned out, or fed up she will go talk to her.\n
    As such, she knew all the ins and outs of her life's business. She became her person to lean on. But the Madame was smart enough not to 
tell her the things nobody needed to know.\n
    Therefore, it took years for Lilian to discover where she hid all the money she inherited from her deceased husband, despite being the one
in charge of organizing the cleaning the house.\n
    But she thought that ending her in order to get the money was morally wrong, so she never did it. At least not until she was absolutely fed
up with her mistreatment.\n
        *Lilian maintains her composure*\n
    My honor, Lilian was not only her greatest confidant, but also her greatest punching bag. She was exposed to a lot of abuse from the victim
during all her period of service. Her virtues and morals were not capable of keeping her resentment towards her in check, so she decided it was
time for Madame to drink her last glass of wine.\n""")


def l_final(mySus):
    """Prints the final sentence Lilian says before starting the minigame
    -mySus:It's the name of the suspect selected"""

    print(f"""\n\nDid I make any mistake?\n
{mySus}'s Lawyer:...\n
Lilian: This is just the by-product of a baseless accusation.Prepare to get your facts straight!\n""")