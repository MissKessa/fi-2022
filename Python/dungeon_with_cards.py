################################################################################
# 
# Computing Basics / Fundamentos de Informática
# University of Oviedo / Universidad de Oviedo
#
# Copyright (c) 2022 Javier Escalada Gómez
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
#
###

import random

CARDS = [
    # Clubs -> Monsters
    ["♣", "A", "M", 17],
    ["♣", 2, "M", 2],
    ["♣", 3, "M", 3],
    ["♣", 4, "M", 4],
    ["♣", 5, "M", 5],
    ["♣", 6, "M", 6],
    ["♣", 7, "M", 7],
    ["♣", 8, "M", 8],
    ["♣", 9, "M", 9],
    ["♣", 10, "M", 10],
    ["♣", "J", "M", 11],
    ["♣", "Q", "M", 13],
    ["♣", "K", "M", 15],

    # Diamonds -> Shields
    ["♦", "A", "S", 11],
    ["♦", 2, "S", 2],
    ["♦", 3, "S", 3],
    ["♦", 4, "S", 4],
    ["♦", 5, "S", 5],
    ["♦", 6, "S", 6],
    ["♦", 7, "S", 7],
    ["♦", 8, "S", 8],
    ["♦", 9, "S", 9],
    ["♦", 10, "S", 10],
    ["♦", "J", "S", 11],
    ["♦", "Q", "S", 11],
    ["♦", "K", "S", 11],

    # Hearts -> Potions
    ["♥", "A", "P", 11],
    ["♥", 2, "P", 2],
    ["♥", 3, "P", 3],
    ["♥", 4, "P", 4],
    ["♥", 5, "P", 5],
    ["♥", 6, "P", 6],
    ["♥", 7, "P", 7],
    ["♥", 8, "P", 8],
    ["♥", 9, "P", 9],
    ["♥", 10, "P", 10],
    ["♥", "J", "P", 11],
    ["♥", "Q", "P", 11],
    ["♥", "K", "P", 11],

    # Spades -> Monsters
    ["♠", "A", "M", 17],
    ["♠", 2, "M", 2],
    ["♠", 3, "M", 3],
    ["♠", 4, "M", 4],
    ["♠", 5, "M", 5],
    ["♠", 6, "M", 6],
    ["♠", 7, "M", 7],
    ["♠", 8, "M", 8],
    ["♠", 9, "M", 9],
    ["♠", 10, "M", 10],
    ["♠", "J", "M", 11],
    ["♠", "Q", "M", 13],
    ["♠", "K", "M", 15],
    
    # Jokers -> Monsters
    ["🃟", "", "M", 21],
    ["🃟", "", "M", 21],
]

MAX_HP = 21


def init_deck():
    deck = list(range(54))
    random.shuffle(deck)
    return deck


def pop_cards(deck, amount):
    cards = deck[:amount]
    deck = deck[amount:]
    return deck, cards


def push_cards(deck, cards):
    deck += cards
    random.shuffle(deck)
    cards = []
    return deck, cards


def card_str(card):
    suit = CARDS[card][0]
    rank = CARDS[card][1]
    type = CARDS[card][2]
    power = CARDS[card][3]
    if type == "S":
        return f"{suit}{rank} Shield({power})"
    if type == "P":
        return f"{suit}{rank} Potion({power})"
    return f"{suit}{rank} Monster({power})"


def show_state(hp, dp, xp):
    print(f"Health: {hp:02d} Defense: {dp:02d} Experience: {xp:02d}")


def show_options(cards):
    print(f"{0:3d}: Run")
    for i, card in enumerate(cards):
        print(f"{i+1:3d}: {card_str(card)}")


def ask_int(prompt):
    while True:
        n = input(prompt)
        if n.lstrip("-").isdigit():
            return int(n)
        print("Please enter a number.")


def ask_int_in_range(prompt, min, max):
    while True:
        n = ask_int(prompt)
        if min <= n <= max:
            return n
        print(f"Please enter a number between {min} and {max}.")


def ask_option(cards, hp, dp, xp):
    show_state(hp, dp, xp)
    show_options(cards)
    min = 0
    max = len(cards)
    return ask_int_in_range(f"Choose from [{min}, {max}]: ", min, max)


def eval_card(card, hp, dp, xp, last_was_potion):
    type = CARDS[card][2]
    power = CARDS[card][3]
    if type == "P":
        if not last_was_potion and hp < MAX_HP:
            old_hp = hp
            hp = min(hp + power, MAX_HP)
            print(f"You heal for {hp-old_hp} health points")
        else:
            print("You wasted the potion")
        last_was_potion = True
    elif type == "S":
        last_was_potion = False
        if dp > 0:
            print(f"You toss away the shield with {dp} defense points")
        dp = power
        print(f"You equip a shield with {dp} defense points")
    else:
        last_was_potion = False
        if dp > 0:
            print(f"Your shield absorbs {dp} attack points")
            dp -= power
            if dp <= 0:
                print("Your shield breaks")
            if dp < 0:
                print(f"You loose {min(hp, -dp)} health points")
                hp = max(hp + dp, 0)
                dp = 0
        else:
            print(f"You loose {min(hp, power)} health points")
            hp = max(hp - power, 0)
        if hp > 0:
            print(f"You kill a monster with {power} health points")
    if hp > 0:
        xp += 1
    return hp, dp, xp, last_was_potion


def main():

    # From: https://patorjk.com/software/taag/#p=testall&f=Bloody&t=Dungeon%20of%20Doom!!!
    print("""
▓█████▄  █    ██  ███▄    █   ▄████ ▓█████  ▒█████   ███▄    █ 
▒██▀ ██▌ ██  ▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▓██  ▒██░▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▓▓█  ░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ▒▒█████▓ ▒██░   ▓██░░▒▓███▀▒░▒████▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒ ░░▒░ ░ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░  ░░░ ░ ░    ░   ░ ░ ░ ░   ░    ░   ░ ░ ░ ▒     ░   ░ ░ 
   ░       ░              ░       ░    ░  ░    ░ ░           ░ 
 ░                                                             
                █     █░ ██▓▄▄▄█████▓ ██░ ██                   
               ▓█░ █ ░█░▓██▒▓  ██▒ ▓▒▓██░ ██▒                  
               ▒█░ █ ░█ ▒██▒▒ ▓██░ ▒░▒██▀▀██░                  
               ░█░ █ ░█ ░██░░ ▓██▓ ░ ░▓█ ░██                   
               ░░██▒██▓ ░██░  ▒██▒ ░ ░▓█▒░██▓                  
               ░ ▓░▒ ▒  ░▓    ▒ ░░    ▒ ░░▒░▒                  
                 ▒ ░ ░   ▒ ░    ░     ▒ ░▒░ ░                  
                 ░   ░   ▒ ░  ░       ░  ░░ ░                  
                   ░     ░            ░  ░  ░                  
                                                               
          ▄████▄   ▄▄▄       ██▀███  ▓█████▄   ██████          
         ▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▒██    ▒          
         ▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌░ ▓██▄            
         ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌  ▒   ██▒         
         ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ▒██████▒▒         
         ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░         
           ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░         
         ░          ░   ▒     ░░   ░  ░ ░  ░ ░  ░  ░           
         ░ ░            ░  ░   ░        ░          ░           
         ░                            ░                        
""")

    amount_cards = 4
    deck = init_deck()
    cards = []
    hp = MAX_HP  # Health points
    dp = 0  # Defense points
    xp = 0  # Experience points
    last_was_potion = False  # Last used card was a potion

    while len(deck):
        print("")
        if len(cards) == 0:
            deck, cards = pop_cards(deck, amount_cards)
        option = ask_option(cards, hp, dp, xp)
        if option == 0:
            deck, cards = push_cards(deck, cards)
            print(f"You run away from the room")
        else:
            card = cards.pop(option - 1)
            hp, dp, xp, last_was_potion = eval_card(card, hp, dp, xp, last_was_potion)
        if hp <= 0:
            break
    show_state(hp, dp, xp)
    if hp <= 0:
        print("You died")
    else:
        print("You win")


main()