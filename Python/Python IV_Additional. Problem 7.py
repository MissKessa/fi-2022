#Python IV_Additional. Problem 7
#Blackjack is a simple, popular card game that is played in many casinos. For simplicity purposes, let's imagine that
#cards value in Blackjack correspond to their number. If you prefer to play with the correct values, please comment
#your code appropriately.
#Two (human) players are playing in our casino and the dealer is the computer (your python script). During a
#round of Blackjack, the players play with the goal of building a hand (a collection of cards) whose cards have a total
#value that is higher than the value of the other's hand, but not over 21. Let's imagine that each player can see only
#his own cards (as if our game were an online game).
#The game logic for our simplified version of Blackjack is as follows.
#• Players ask cards in turns.
#• They have three turns maximum.
#• If, at any point, the value of the player's hand exceeds 21, the player loses immediately and the other wins.
#• At any point prior to lose or finish the turns, each player may "stand" (plantarse).
#• At the end, the player with higher punctuation wins.

import random;
player1_points=0
player2_points=0
win_player1=False

turns=3
print("Player 1 is your turn")
while turns>0:
    card=random.randint(1,13)
    if card==11 or card==12 or card==13:
        card=10
    
    player1_points+=card
    print("Player 1 has:",player1_points)
    if turns!=1:
        continue_turn=input("Do you want to continue?: ")
        if continue_turn.lower()=="no" or player1_points>=21:
            break
    turns-=1
if player1_points==21:
    win_player1=True
#if player1_points==21:
    #print("Player 1 wins")
#elif player1_points>21:
    #print("Player 2 wins")
if win_player1==False:
    turns=3
    print("\nPlayer 2 is your turn")
    while turns>0:
        card=random.randint(1,13)
        if card==11 or card==12 or card==13:
            card=10
        
        player2_points+=card
        print("Player 2 has:",player2_points)
        if turns!=1:
            continue_turn=input("Do you want to continue?: ")
            if continue_turn.lower()=="no" or player2_points>=21:
                break
    turns-=1
if player2_points>21:
    win_player1=True
elif player1_points>player2_points:
    win_player1=True
elif player1_points>player2_points:
    print("Tie")

if win_player1==True:
    print("Player 1 wins")
else:
    print("Player 2 wins")
#if player2_points>21:
  #  print("Player 1 wins")
#elif player2_points>player1_points or player1_points>21:
 #   print("Player 2 wins")
#elif player2_points==player1_points:
  #  print("Tie")
#else:
  #  print("Player 2 lose")