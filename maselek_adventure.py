title = "ON A WALK THROUGH A SNOWY FOREST \nby Jozef Maselek"
intro = "you wake up in your home to find that it had snowed heavily overnight! \nYou decide that you want to walk through the woods and take a nice walk."
input_1 = (" \nPress the <Enter> key to continue.")
description_1 = ""
input_2 = (" \nWould you like to know more about whats happening?")
description_2 = ""

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
    description_1 = "You wake up to coldness of your house. \nYou decide to put on some warm clothes and boots before going outside to get something to eat and drink at the pub."
    print(description_1)
    input(input_1)

def village():
    description_1 = "You exit your home to the snappy and frigid morning air. \nSnow covers everything around you and the sun is blocked out by gray clouds. You decide to shovel your driveway later."
    print("")
    print(description_1)
    input(input_2)
    description_2 = "The pub is up the road a fair bit from your home so you get to walking."
    print(description_2)
    input(input_1)

def pub():
    print("")
    description_1 = "You enter the pub to see that its mostly empty. Some of your neighbors are enjoying breakfast and coffee. \nYou find a seat and order a full English. You also order yourself a coffee. \nYou finish your food and go back outside."
    print(description_1)
    input(input_2)
    description_2 = "The food was sorta cold, but the coffee filled your stomach with warmth. There was a girl with an umbrella making small talk to the man at the bar."
    print(description_2)
    input(input_1)

def frozen_lake():
    print("")
    description_1 = "You walk out of the village towards the now frozen lake nearby. \nA small bit of the lake still visible as the mouth of a river is flowing into it."
    print(description_1)
    input(input_2)
    description_2 = "A meadow borders the lake in the direction your walking. You can also hear a train blow its whistle in the distance."
    print(description_2)
    input(input_1)
    

def meadow():
    print("")
    description_1 = "A lone tree stands in the middle of the meadow. You see some birds flying to and from the tree as you're walking by."
    print(description_1)
    input(input_2)
    description_2 = "You see the river ahead of you and keep walking towards it. The birds are very loud to each other, and it seems like there are more hidden in the tree."
    print(description_2)
    input(input_1)
    


def river():
    print("")
    description_1 = "The river still flows despite the frigid temperature. Its a very bright blue."
    print(description_1)
    input(input_2)
    description_2 = "You take your hand out of its glove and test the water. \nYou find that its cold."
    print(description_2)
    description_1 = "You keep walking along the river."
    print(description_1)
    input(input_1)
    


def campsite():
    print("")
    description_1 = "You see an old campsite on the other side of the river. \nYou decide to head towards it and forge the river by walking over some rocks."
    print(description_1)
    input(input_2)
    description_2 = "The campsite is fairly new, but the coals in the firepit are icy to the touch. \nSome snowed on, leftover tents make up the rest of the campsite."
    print(description_2)
    description_1 = "You head further into the woods surrounding the campsite, towards cliffs you can see in the distance."
    print(description_1)
    input(input_1)
    


def swamp():
    print("")
    description_1 = "You eventually find yourself in an ice-covered swamp. Trees sprout from small land masses throughout the swamp."
    print(description_1)
    input(input_2)
    description_2 = "You stop and notice a deer on the far side of the swamp. \nBefore you can move again, it notices you and runs away."
    print(description_2)
    description_1 = "You carefully walk over the ice of the swamp."
    print(description_1)
    input(input_1)
    


def cliffs():
    print("")
    description_1 = "You find yourself at the base of the cliffs. You look above you and see more cliffs jutting out on top of each other."
    print(description_1)
    input(input_2)
    description_2 = "\nA small pathway can be seen clearly carved along the cliffside going towards the top."
    print(description_2)
    description_1 = "You follow the pathway."
    print(description_1)
    input(input_1)
    


def rock():
    print("")
    description_1 = "You make your way to the top of the cliffside and find yourself graced by the presence of a large rock."
    print(description_1)
    input(input_2)
    description_2 = "You take a look around you and decide to take a picture of your surroundings. \nhttps://cdn.discordapp.com/attachments/311944103804010496/1020799631766069331/unknown.png"
    print(description_2)
    input("Press the <Enter> key to end.")
    


def end():
    print("")
    print("Thank you for your time. \nGoodbye!")



main()