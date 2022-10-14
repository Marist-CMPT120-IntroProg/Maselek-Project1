title = "ON A WALK THROUGH A SNOWY FOREST \nby Jozef Maselek"
input_1 = (" \nPress the <Enter> key to continue.")
description_1 = ""
input_2 = (" \nWould you like to know more about whats happening?")
description_2 = ""
actions = ["north","south","east","west","quit","help", "examine"]
stops = 0
ask = "What do you want to go, where do you want to go?"

## There is defintely a way to make the "while" loops dependent on a function with paramaters to serve the location selections (RIGHT?????)

print("")
print("")
print(title)
print("")
userName = input("What is your name?")



def main():
    
    
    intro = f"You, {userName}, wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to take a nice walk through the woods."
    print("")
    print(intro)
    input(input_1)

    ## also change to jupiter notebook
    ##
    ## example
    ## cmd = input("where do you want to go: ")
    ## if cmd.upper() = "NORTH"
    ##   rest of code
    
    home()
    
    

def help():
    print("")
    print("Your options are: north, south, east, west, quit, help, examine")
    print("Good luck!")
    input(input_1)

def home():
    location = ""
    print("")
    ##stops = stops +1
    description_1 = "You wake up to coldness of your house. \nYou decide to put on some warm clothes and boots before going outside to get something to eat and drink at the pub."
    description_2 = "Your home smells like a cross between a Stop & Shop and Minnesota."


    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "south":
            location = "village"
            village()
        elif userInput.lower == "north":
            location = "village"
            village()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            home()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            home()

def village():
    ##stops = stops +1
    description_1 = "You exit to the snappy and frigid morning air. \nSnow covers everything around you and the sun is blocked out by gray clouds. You decide to shovel your driveway later."
    print("")
    ##print(description_1)
    ##input(input_2)
    description_2 = "The pub is up the road a fair bit from your home so you get to walking. \nYou can also go south to the lake."
    ##print(description_2)

    description_3 = "For some odd reason, the snow on the sidewalk seems to be cleared out from people walking through it."

    userInput = ""
    while userInput not in actions:
        print(description_1)
        print(description_2)

        print(ask)

        userInput = input()
        if userInput.lower == "east":
            location = "pub"
            pub()
        elif userInput.lower == "north":
            location = "pub"
            pub()
        elif userInput.lower == "south":
            location = "lake"
            frozen_lake()
        elif userInput.lower == "examine":
            print("")
            print(description_3)
            print("")
            print("")
            village()
        elif userInput.lower == "help":
            help()
            village()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            village()

def pub():
    ####stops = stops +1
    print("")
    description_1 = "You enter the pub to see that its mostly empty. Some of your neighbors are enjoying breakfast and coffee. \nYou find a seat and order a full English. You also order yourself a coffee. \nYou finish your food and go back outside."
    ##print(description_1)
    ##input(input_2)
    description_2 = "The food was sorta cold, but the coffee filled your stomach with warmth. There was a girl with an umbrella making small talk to the man at the bar."
    ##print(description_2)

    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "south":
            location = "village"
            village()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            pub()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            pub()

def frozen_lake():
    ##stops = stops +1
    print("")
    description_1 = "You walk out of the village towards the now frozen lake nearby. \nA small bit of the lake still visible as the mouth of a river is flowing into it."
    ##print(description_1)
    ##input(input_2)
    description_2 = "A meadow borders the lake in the direction your walking. You can also hear a train blow its whistle in the distance."
    ##print(description_2)

    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "south":
            location = "meadow"
            meadow()
        elif userInput.lower == "north":
            location = "village"
            village()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            home()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            frozen_lake()
    

def meadow():
    ##stops = stops +1
    print("")
    description_1 = "A lone tree stands in the middle of the meadow. You see some birds flying to and from the tree as you're walking by."
    ##print(description_1)
    ##input(input_2)
    description_2 = "You see the river ahead of you as you are walking. The birds are very loud to each other, and it seems like there are more hidden in the tree."
    ##print(description_2)

    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "south":
            location = "river"
            river()
        elif userInput.lower == "north":
            location = "lake"
            frozen_lake()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            meadow()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            meadow()
    


def river():
    ##stops = stops +1
    print("")
    description_1 = "The river still flows despite the frigid temperature. Its a very bright blue."
    ##print(description_1)
    ##input(input_2)
    description_2 = "You take your hand out of its glove and test the water. \nYou find that its cold."
    ##print(description_2)
    description_3 = "You keep walking along the river. You also see an old campsite on the western side of the river."
    ##print(description_1)

    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "west":
            location = "campsite"
            campsite()
        elif userInput.lower == "south":
            location = "river"
            river()
        elif userInput.lower == "north":
            location = "meadow"
            meadow()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print(description_3)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            river()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            river()
    


def campsite():
    ##stops = stops +1
    print("")
    description_1 = "You decide to head towards it and forge the river by walking over some rocks."
    ##print(description_1)
    ##input(input_2)
    description_2 = "The campsite is fairly new, but the coals in the firepit are icy to the touch. \nSome snowed on leftover tents make up the rest of the campsite."
    ##print(description_2)
    description_3 = "You see a swamp bordering the northern side of the campsite and an array of cliffs past it."
    ##print(description_1)

    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "north":
            location = "swamp"
            swamp()
        elif userInput.lower == "east":
            location = "river"
            river()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print(description_3)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            campsite()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            campsite()
    


def swamp():
    ##stops = stops +1
    print("")
    description_1 = "You eventually find yourself in an ice-covered swamp. Trees sprout from small land masses throughout the swamp."
    ##print(description_1)
    ##input(input_2)
    description_2 = "You stop and notice a deer on the far side of the swamp. \nBefore you can move again, it notices you and runs away."
    ##print(description_2)
    description_3 = "You carefully walk over the ice of the swamp."
    ##print(description_1)
    
    userInput = ""
    while userInput not in actions:
        print(description_1)

        print(ask)

        userInput = input()
        if userInput.lower == "south":
            location = "campsite"
            campsite()
        elif userInput.lower == "north":
            location = "cliffs"
            cliffs()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print(description_3)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            swamp()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            swamp()
    


def cliffs():
    ##stops = stops +1
    print("")
    description_1 = "You find yourself at the base of the cliffs. You look above you and see more cliffs jutting out on top of each other."
    ##print(description_1)
    ##input(input_2)
    description_2 = "\nA small pathway can be seen clearly carved along the cliffside going north towards the top."
    ##print(description_2)
    ##description_3 = "You follow the pathway."
    ##print(description_1)
    
    userInput = ""
    while userInput not in actions:
        print(description_1)
  
        print(ask)
        
        userInput = input()
        if userInput.lower == "south":
            location = "swamp"
            swamp()
        elif userInput.lower == "north":
            location = "rock"
            rock()
        elif userInput.lower == "examine":
            print("")
            print(description_2)
            print("")
            print("")
            home()
        elif userInput.lower == "help":
            help()
            cliffs()
        elif userInput.lower == "quit":
            break
        else: 
            print("")
            print("Please enter a valid option.")
            cliffs()
    


def rock():
    ##stops = stops +1
    print("")
    description_1 = "You make your way to the top of the cliffside and find yourself graced by the presence of a large rock."
    print(description_1)
    input(input_2)
    description_2 = "You take a look around you and decide to take a picture of your surroundings. \nhttps://cdn.discordapp.com/attachments/311944103804010496/1020799631766069331/unknown.png"
    print(description_2)
    input("Press the <Enter> key to end.")
    end()
    


def end():
    print("")
    print(f"Thank you for your time, {userName}. \nGoodbye!")
    print(f"You went through {stops} areas!")

    ##copyright
    print("")
    print("Game idea, name, and title all copyrighted by Jozef Maselek, \nany and all online interaction is not rated by ESRB nor monitored by Jozef Maselek")




main()