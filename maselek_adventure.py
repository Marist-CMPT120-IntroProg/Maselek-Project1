from locale_1 import *
from world import *
from player import *


# ------------------- variables ----------------

ask: str = "\nWhat direction do you want to go in?"
input_1: str = (" \nPress the <Enter> key to continue.")
title: str = "ON A WALK THROUGH A SNOWY FOREST \nby Jozef Maselek"
userName = None

# -------------------- functionsal -------------------


def intro():
    global userName
    global world1
    global player1

    world1 = World()
    player1 = Player(userName, world1)

    print("")
    print("")
    print(title)
    print("")
    userName= input("What is your name?")
    intro = f"You, {userName}, wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to take a nice walk through the woods."
    print("")
    print(intro)
    input(input_1)

    print(world1.areas[0].summary)
    world1.areas[0].was_visited = True

def end():
    global userName

    print("")
    print(f"Thank you for your time, {userName}. \nGoodbye!")
    print(f"You went through {stops} areas!")

    ##copyright
    print("")
    print("")
    print("Game idea, name, and title all copyrighted by Jozef Maselek, \nany and all online interaction is not rated by ESRB nor monitored by Jozef Maselek")

def help():
    print("")
    print("")
    print("Your options are: north, south, east, west, details, help, and quit")
    print("Good luck!")
    input(input_1)

# ----------------------- GAME LOOP ------------------------

def main_game():
    
    global actions
    global direction
    global stops
    
    intro()
    actions = ["north", "south", "east", "west", "details", "help", "quit"]
    stops = player1.stops

    while True:
        user_movement = input(ask).lower() 
        
        if user_movement in actions:
            
            # north
            if user_movement == actions[0]:
                direction = 1
                player1.move_check(direction)
            # south
            elif user_movement == actions[1]: 
                direction = 2
                player1.move_check(direction)
            # east
            elif user_movement == actions[2]:
                direction = 3
                player1.move_check(direction)
            # west    
            elif user_movement == actions[3]: 
                direction = 4
                player1.move_check(direction)


            # details
            elif user_movement == actions[4]: 
                player1.details(player1.current_loc)
            
            # help
            elif user_movement == actions[5]: 
                help()
            
            # quit            
            elif user_movement == actions[6]: 
                break
            

        else: 
            print("\nPlease enter a valid command")
            continue
    
    end()


## ----------- main -----------

def main():
    main_game()

main()