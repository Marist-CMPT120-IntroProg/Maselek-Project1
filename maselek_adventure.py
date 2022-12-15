from locale_1 import *
from world import *
from player import *
#from graphics import *
#from button import Button


# ------------------- variables ----------------

ask: str = "\nWhat direction do you want to go in? Or what do you want to do?"
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
    userName = input("What is your name?")
    print("")
    intro = f"You, {userName}, wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to take a nice walk through the woods."
    print(intro)
    input(input_1)
    print("")

    print(world1.areas[0].summary)
    world1.areas[0].was_visited = True

def end():
    global userName

    print("")
    print(f"Thank you for your time, {userName}. \nGoodbye!")
    print(f"You went through {stops} areas!")
    print(f"you gained {score} score!")

    ##copyright
    print("")
    print("")
    print("Game idea, name, and title all copyrighted by Jozef Maselek, \nany and all online interaction is not rated by ESRB nor monitored by Jozef Maselek")

def help():
    print("")
    print("")
    print("Your options are: north, south, east, west, details, talk, help, and quit")
    print("Good luck!")
    input(input_1)

# ----------------------- GAME LOOP ------------------------


def main_game():
    
    global actions
    global direction
    global stops
    global score
    
    intro()

    actions = ["north", "south", "east", "west", "details", "talk", "help", "quit"]
    stops = player1.stops
    score = player1.score

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
            
            # talk
            elif user_movement == actions[5]:
                player1.talk()

            # help
            elif user_movement == actions[6]: 
                help()
            
            # quit            
            elif user_movement == actions[7]: 
                break
            

        else: 
            print("\nPlease enter a valid command")
            continue
    
    end()


## ----------- main -----------

def main():
    main_game()
    #userNameEntry_gui()
   
main()

## I ORIGINALLY TRIED TO DO GUI but it just isn't keyed to the way that my code is programmed and I didn't wnat to figure out/chang my original code. I also don't want to 
## delete it just cause so I'm leaving it here.
def failedgui():

    def userNameEntry_gui():

        userName_window = GraphWin("name", 400,200)
        userName_window.setCoords(0, 0, 10, 10)

        userName_ask = Text(Point(5, 8), "What is your name?")
        userName_ask.setFill("blue")
        userName_ask.setOutline("gray")
        userName_ask.setSize(18)
        userName_ask.draw(userName_window)

        userName_entry = Entry(Point(5, 6), 20)
        userName_entry.draw(userName_window)

        start_btn = Button(userName_window, Point(5, 2), 2, 1, "Start")
        start_btn.activate()

        while userName_window.isOpen():
            click_pos = userName_window.getMouse()

            if start_btn.clicked(click_pos):
                
                intro_gui(userName_entry.getText())
                userName_window.close()




    def intro_gui(usersName):

        

        intro_window = GraphWin("intro", 600, 400)
        intro_window.setCoords(0, 0, 10, 10)

        title_text = Text(Point(5, 8), title)
        title_text.setFill("blue")
        title_text.setOutline("gray")
        title_text.setSize(18)
        title_text.setStyle("bold")
        title_text.draw(intro_window)

        intro_text = Text(Point(5, 4), f"You, {usersName}, wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to take a nice walk through the woods.")
        intro_text.setFill("gray")
        intro_text.setOutline("blue")
        intro_text.setSize(10)
        intro_text.draw(intro_window)

        start_btn = Button(intro_window, Point(5, 2), 2, 1, "Start")
        start_btn.activate()

        while intro_window.isOpen():
            click_pos = intro_window.getMouse()

            if start_btn.clicked(click_pos):
                
                main_game_gui(usersName)
                intro_window.close()

    def showLocation(move):
        location = GraphWin("location", 300, 100)
        Text(Point(2, 2), move).draw(location)

    def main_game_gui(player_name):

        global actions
        global direction
        global stops

        global world1
        global player1

        world1 = World()
        player1 = Player(player_name, world1)
        stops = player1.stops

        app = GraphWin("main_game", 800, 800)
        app.setCoords(0, 0, 10, 10)

        

        north_btn = Button(app, Point(2, 4), 2, 1, "North")
        south_btn = Button(app, Point(4, 4), 2, 1, "South")
        east_btn = Button(app, Point(6, 4), 2, 1, "East")
        west_btn = Button(app, Point(8, 4), 2, 1, "West")

        details_btn = Button(app, Point(3,2), 2, 1, "Details")
        details_btn.activate()

        help_btn = Button(app, Point(7,2), 2, 1, "Help")
        help_btn.activate()

        quit_btn = Button(app, Point(9, 9.5), 2, 1, "Quit")
        quit_btn.activate()

        replay_btn = Button(app, Point(1, 9.5), 2, 1, "Play Again")
        replay_btn.activate()


        def activate_all():
            north_btn.activate()
            south_btn.activate()
            east_btn.activate()
            west_btn.activate()
        activate_all()

        def deactivate_all():
            north_btn.deactivate()
            south_btn.deactivate()
            east_btn.deactivate()
            west_btn.deactivate()

        youAreAt_text = Text(Point(5, 5), "idk")
        youAreAt_text.setFill("blue")
        youAreAt_text.setOutline("gray")
        youAreAt_text.setSize(10)
        youAreAt_text.setStyle("bold")
        youAreAt_text.draw(app)

        while app.isOpen():
            click_pos = app.getMouse()

            #north
            if north_btn.clicked(click_pos):
                direction = 1
                showLocation(player1.move_check(direction))

                
            #south      
            elif south_btn.clicked(click_pos):
                direction = 2
                showLocation(player1.move_check(direction))

                
            #east
            elif east_btn.clicked(click_pos):
                direction = 3
                showLocation(player1.move_check(direction))


            #west
            elif west_btn.clicked(click_pos):
                direction = 4
                showLocation(player1.move_check(direction))


            #details
            elif details_btn.clicked(click_pos):
                showLocation(player1.move_check(direction))
                

            #help
            elif help_btn.clicked(click_pos):
                help()
            
            #quit
            elif quit_btn.clicked(click_pos):
                break

            #replay
            if replay_btn.clicked(click_pos):
                
                intro_gui()
                app.close()
        

        
            