import Input_Output
import Games
import Events
import characters

rooms=Input_Output.assign_keys(Input_Output.list_rooms)

reputation=100
energy=20
day=0 #max 10
death=False

Input_Output.print_title()
Input_Output.print_story()
Input_Output.print_tutorial()

Input_Output.create_notes()

murderer=characters.sus_selection(characters.suspects)
detective=Input_Output.ask_player_name()


#INTERROGATORIO###
Events.the_interrogation(detective,murderer)

#INVESTIGATION
Input_Output.print_full_map()
Input_Output.print_day(day)

win=True

print("""When I go to the house, I see that the rooms have a padlock on the door. I don't know how I could open them.
Let's go to the garden""")
while True:
    energy,reputation,day=Events.pool(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break

    Events.random_event(reputation,1,murderer,characters.suspects)
    Input_Output.ask_code("Outside",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.the_office(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break

    Events.random_event(reputation,2,murderer,characters.suspects)
    Input_Output.ask_code("Office",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.library(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break

    Events.random_event(reputation,3,murderer,characters.suspects)
    Input_Output.ask_code("Library",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.casino(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,4,murderer,characters.suspects)
    Input_Output.ask_code("Casino",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.living_room(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,5,murderer,characters.suspects)
    Input_Output.ask_code("Living Room",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.the_sons_bedroom(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,6,murderer,characters.suspects)
    Input_Output.ask_code("Son's Bedroom",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.kitchen(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,7,murderer,characters.suspects)
    Input_Output.ask_code("Kitchen",rooms)
    Input_Output.show_notes()

    energy,reputation,day=Events.master_bedroom(energy,reputation,murderer,characters.suspects,rooms,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,8,murderer,characters.suspects)
    Input_Output.ask_code("Master Bedroom",rooms)
    Input_Output.show_notes()

    energy,reputation,day,death=Events.the_bathroom(energy,reputation,murderer,day)
    win,skip=Input_Output.skip_game(reputation,day,win)
    if skip:
        break
    
    Events.random_event(reputation,9,murderer,characters.suspects)
    Input_Output.show_notes()
    break



if win:
    ask=input("Before going to the trial, I think that memorising the notes. Will be a good idea.\nI read them? (yes/no)\n").strip().lower()    
    if ask=="yes":
        Input_Output.read_file("Notes.txt")
    
    per_points=Games.main_trial(detective,murderer)
elif death:
    print(f"""...but not on your own feet.
After everything you've gone through, it was worthless... You kept investigating only for you to end like this. What a pity...
Your funeral has now started. Everyone you cared for is there, even your boss has come.

REST IN PEACE
{detective.upper()}\n""")

    per_points=0
    win=False
else:
    print(f"""\n\nYour boss is out looking at you with a serious face:
-Boss: I know you couldn't do the job. You are fired with me your badge
-{detective}: But...
-Boss: Now! \n
I give the badge to him and he leaves. When I look to the left, I see {(murderer["name"])} with a psychopath smile.
I can't believe this is the end of my career""")
    per_points=0


Input_Output.write_final_score(detective,day,reputation,per_points,win)
Input_Output.read_file("Final Scores.txt")
Input_Output.print_credits()