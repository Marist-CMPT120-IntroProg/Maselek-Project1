

# ----------- data dictionary area !!! --------------
areas = {
    "home": {"name": "Home", "south": "village", "north": "village",
        "summary": "You wake up to the coldness of your house. \nYou decide to put on some warm clothes and boots before going outside to get something to eat and drink at the pub.", "details": "Your home smells like a cross between a Stop & Shop and Minnesota.", 
        "was_visited": False},
    "village": {"name": "The Village", "east": "pub", "north": "pub", "south": "frozen_lake",
        "summary": "You exit to the snappy and frigid morning air. \nSnow covers everything around you and the sun is blocked out by gray clouds. You decide to shovel your driveway later.", "details": "The pub is up the road a fair bit from your home so you get to walking. \nYou can also go south to the lake.\nFor some odd reason, the snow on the sidewalk seems to be cleared out from people walking through it.", 
        "was_visited": False},
    "pub": {"name": "The Pub", "south": "village",
        "summary": "You enter the pub to see that its mostly empty. Some of your neighbors are enjoying breakfast and coffee. \nYou find a seat and order a full English. You also order yourself a coffee. \nYou finish your food and go back outside.", "details": "The food was sorta cold, but the coffee filled your stomach with warmth. There was a girl with an umbrella making small talk to the man at the bar.", 
        "was_visited": False},
    "frozen_lake": {"name": "The Frozen Lake", "south": "meadow", "north": "village",
        "summary": "You walk out of the village towards the now frozen lake nearby. \nA small bit of the lake still visible as the mouth of a river is flowing into it.", "details": "A meadow borders the lake in the direction your walking. You can also hear a train blow its whistle in the distance.", 
        "was_visited": False},
    "meadow": {"name": "The Meadow", "south": "river", "north": "frozen_lake",
        "summary": "A lone tree stands in the middle of the meadow. You see some birds flying to and from the tree as you're walking by.", "details": "You see the river ahead of you as you are walking. The birds are very loud to each other, and it seems like there are more hidden in the tree.", 
        "was_visited": False},
    "river": {"name": "The River", "west": "campsite", "south": "river", "north": "meadow",
        "summary": "The river still flows despite the frigid temperature. Its a very bright blue.", "details": "You take your hand out of its glove and test the water. \nYou find that its cold.\nYou keep walking along the river. You also see an old campsite on the western side of the river.", 
        "was_visited": False},
    "campsite": {"name": "The Campsite", "north": "swamp", "east": "river",
        "summary": "You decide to head towards it and forge the river by walking over some rocks.", "details": "The campsite is fairly new, but the coals in the firepit are icy to the touch. \nSome snowed on leftover tents make up the rest of the campsite.\nYou see a swamp bordering the northern side of the campsite and an array of cliffs past it.", 
        "was_visited": False},
    "swamp": {"name": "The Swamp", "south": "campsite", "north": "cliffs",
        "summary": "You eventually find yourself in an ice-covered swamp. Trees sprout from small land masses throughout the swamp.", "details": "You stop and notice a deer on the far side of the swamp. \nBefore you can move again, it notices you and runs away.\nYou carefully walk over the ice of the swamp.", 
        "was_visited": False},
    "cliffs": {"name": "The Cliffs", "south": "swamp", "north": "rock",
        "summary": "You find yourself at the base of the cliffs. You look above you and see more cliffs jutting out on top of each other.", "details": "A small pathway can be seen clearly carved along the cliffside going north towards the top", 
        "was_visited": False},
    "rock": {"name": "The Rock", 
        "summary": "You make your way to the top of the cliffside and find yourself graced by the presence of a large rock. \nThis is the end of the game, type 'end' to finish the game", "details": "You take a look around you and decide to take a picture of your surroundings. \nhttps://cdn.discordapp.com/attachments/311944103804010496/1020799631766069331/unknown.png", 
        "was_visited": False},
    }
current_area = areas["home"]



# ------------------- ACTIONS ----------------
actions: str = ["north", "south", "east", "west", "quit", "help", "details", "end"]
ask: str = "\nWhat direction do you want to go in?"
input_1: str = (" \nPress the <Enter> key to continue.")
title: str = "ON A WALK THROUGH A SNOWY FOREST \nby Jozef Maselek"
stops: int = 1



# --------------------- GAME INTRO -----------------
print("")
print("")
print(title)
print("")
userName: str = input("What is your name?")
intro = f"You, {userName}, wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to take a nice walk through the woods."
print("")
print(intro)
input(input_1)




# --------------------- END AND HELP FUNCTIONS --------------------
def end():
    print("")
    print(f"Thank you for your time, {userName}. \nGoodbye!")
    print(f"You went through {stops} areas!")

    ##copyright
    print("")
    print("Game idea, name, and title all copyrighted by Jozef Maselek, \nany and all online interaction is not rated by ESRB nor monitored by Jozef Maselek")



def help():
    print("")
    print("Your options are: north, south, east, west, quit, help, details")
    print("Good luck!")




# ----------------------- GAME LOOP ------------------------
while True:
    # display current location
    print("")
    print("You are in {}.".format(current_area["name"]))
    print("")

    print(current_area["summary"])

    userInput = input(ask)
    if userInput in actions:
        if userInput.lower() == "help":
            help()
            input(input_1)

        elif userInput.lower() == "quit":
            break
        
        elif userInput.lower() == "end":
            end()
            break

        elif userInput.lower() == "details":
            print("")
            print(current_area["details"])
            input(input_1)
        

        elif userInput in current_area:
            if current_area["was_visited"] == False:
                stops = stops + 1
                current_area["was_visited"] == True
            current_area = areas[current_area[userInput]]
        else:
            print("")
            print("")
            print("You can't go that way.")
            input(input_1)

    else:
        print("")
        print("Please enter a valid option")
        input(input_1)