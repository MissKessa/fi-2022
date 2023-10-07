#Python VI. Problem 31

def str_to_list(text):
 """Returns a list of strings according to the following
    rules: 
    i) eliminate any occurrence of the text ”and”
    ii) separate the strings using the comma symbol (’,’)
    iii) eliminate any leading or ending white space."""


def city_and_country(text):
    """receives the string corresponding to one of the valid places and returns a list 
    with two strings: the city name and the country at positions 0 and 1, correspondingly."""


def fusion(name, job, place, fee):
    """The function should return a list with the four values in the given order."""


def merge(names,jobs, places, fees):
 """Receives 4 lists containing names, jobs, places and fees, respectively.
    This function should generate a 100 elements list, each element contain a list
    with a random name, a random job, a random place and a random fee"""


def list_to_str(L):
    """Receiving a list L of elements returns a string that:
    i) converts the list L to a list of strings by joining the each of
    its elements with the comma character (’,’) -maybe it is interesting to remember you
    the str’s method join
    ii) joining all the elements of L with the character new line ('\n')."""
    

def count_letters(full_name):
    """Return the number of letters within the name (do not including the surname letters!)"""
    counter=0
    for i in range(0,len(full_name),1):
        while fullname[i]!=" ":
            counter++
        break
    return counter
            
    

names = "Deep Toot, Wikipedia Brown, Toots Magoots, George Washingturd, Zeus Toots, Queen, Kong, John Marmalade, Mr. E. Sir, Smalls Assquatch, and Joe Bag O' Doughnuts"
jobs = "Dog Food Tester, Note Taker for College Students, Gum Buster, Phone Psychic, Chicken Sexer, Jelly Doughnut Filler, Stand-in Bridesmaid, Golf Ball Diver, Odor Judges, Potato Chip Inspector, and Egg Inspector"
places = "Okay (Oklahoma, USA), Tubbercurry (Ireland), Boring (Oregon, USA), Dull (Scotland), Fuckersberg (Austria), Scratchy Bottom (Devon, UK), Tyewhoppety (Kentucky, USA), Ken-Taco-Huts (New Mexico, USA), Ding Dong (Texas, USA), Blubberhouses (Yorkshire, UK), Satan's Kingdom (Vermont, USA), Moron (Mongolia, Russia), The Finger Lakes (NY, USA), and Coxsackie (NY, USA)"
fees = [300, 35, 45, 64, 120, 95, 65, 80, 250, 76, 98]