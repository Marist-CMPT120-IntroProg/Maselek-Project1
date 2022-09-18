title = "ON A WALK THROUGH A SNOWY FOREST \nby Jozef Maselek"
intro = "you wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to walk through the woods and take a nice walk."
input_1 = (" \nPress the <Enter> key to continue.")
description = "You wake up to coldness of your house. \nYou decide to put on some warm clothes and boots before going outside to get something to eat and drink at the pub."


def main():
    stops = 0
    print("")
    print("")
    print(title)
    print("")
    print(intro)
    input(input_1)

    home()
    stops = stops +1
    village()
    stops = stops +1
    pub()
    stops = stops +1
    frozen_lake()
    stops = stops +1
    meadow()
    stops = stops +1
    river()
    stops = stops +1
    campsite()
    stops = stops +1
    swamp()
    stops = stops +1
    cliffs()
    stops = stops +1
    rock()
    stops = stops +1
    end()
    
    print(f"You went through {stops} areas!")

def home():
    print("")
    print(description)
    input(input_1)

def village():
    description = "You exit your home to the snappy and frigid morning air. \nSnow covers everything around you and the sun is blocked out by gray clouds. You decide to shovel your driveway later."
    print("")
    print(description)
    ##print("The pub is up the road a fair bit from your home so you get to walking.")
    input(input_1)

def pub():
    print("")
    description = "You enter the pub to see that its mostly empty. Some of your neighbors are enjoying breakfast and coffee. \nYou find a seat and order a full English. You also order yourself a coffee. \nYou finish your food and go back outside."
    print(description)
    input(input_1)

def frozen_lake():
    print("")
    description = "You walk out of the village towards the now frozen lake nearby. \nA small bit of the lake still visible as the mouth of a river is flowing into it."
    ##print("A meadow borders the lake in the direction your walking.")
    print(description)
    input(input_1)
    

def meadow():
    print("")
    description = "A lone tree stands in the middle of the meadow. You see some birds flying to and from the tree as you're walking by."
    ##print("You see the river ahead of you and keep walking towards it.")
    print(description)
    input(input_1)
    


def river():
    print("")
    description = "The river still flows despite the frigid temperature. Its a very bright blue."
    ##print("You take your hand out of its glove and test the water. \nYou find that its cold.")
    print(description)
    description = "You keep walking along the river."
    print(description)
    input(input_1)
    


def campsite():
    print("")
    description = "You see an old campsite on the other side of the river. \nYou decide to head towards it and forge the river by walking over some rocks."
    ##print("The campsite is fairly new, but the coals in the firepit are icy to the touch. \nSome snowed on, leftover tents make up the rest of the campsite.")
    print(description)
    description = "You head further into the woods surrounding the campsite, towards cliffs you can see in the distance."
    print(description)
    input(input_1)
    


def swamp():
    print("")
    description = "You eventually find yourself in an ice-covered swamp. Trees sprout from small land masses throughout the swamp."
    ##print("You stop and notice a deer on the far side of the swamp. \nBefore you can move again, it notices you and runs away.")
    print(description)
    description = "You carefully walk over the ice of the swamp."
    print(description)
    input(input_1)
    


def cliffs():
    print("")
    description = "You find yourself at the base of the cliffs. You look above you and see more cliffs jutting out on top of each other.\nA small pathway can be seen clearly carved along the cliffside going towards the top."
    print(description)
    description = "You follow the pathway."
    print(description)
    input(input_1)
    


def rock():
    print("")
    description = "You make your way to the top of the cliffside and find yourself graced by the presence of a large rock."
    ##print("You take a look around you and decide to take a picture of your surroundings.")
    ##print("https://cdn.discordapp.com/attachments/311944103804010496/1020799631766069331/unknown.png")
    print(description)
    input("Press the <Enter> key to end.")
    


def end():
    print("")
    print("Thank you for your time. \nGoodbye!")



main()