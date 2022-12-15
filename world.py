import locale_1

## text variables
home1: str = "You wake up to the coldness of your house. \nYou decide to put on some warm clothes and boots before going outside to get something to eat and drink at the pub."
home2: str = "Your home smells like a cross between a Stop & Shop and Minnesota."
village1: str = "You exit to the snappy and frigid morning air. \nSnow covers everything around you and the sun is blocked out by gray clouds. You decide to shovel your driveway later."
village2: str = "The pub is up the road a fair bit from your home so you get to walking. \nYou can also go south to the lake.\nFor some odd reason, the snow on the sidewalk seems to be cleared out from people walking through it."
pub1: str = "You enter the pub to see that its mostly empty. Some of your neighbors are enjoying breakfast and coffee. \nYou find a seat and order a full English. You also order yourself a coffee. \nYou finish your food and go back outside. There is somedbody you can talk to."
pub2: str = "The food was sorta cold, but the coffee filled your stomach with warmth. There was a girl with an umbrella making small talk to the man at the bar."
frozen_lake1: str = "You walk out of the village towards the now frozen lake nearby. \nA small bit of the lake still visible as the mouth of a river is flowing into it."
frozen_lake2: str = "A meadow borders the lake in the direction your walking. You can also hear a train blow its whistle in the distance."
meadow1: str = "A lone tree stands in the middle of the meadow. You see some birds flying to and from the tree as you're walking by."
meadow2: str = "You see the river ahead of you as you are walking. The birds are very loud to each other, and it seems like there are more hidden in the tree."
river1: str = "The river still flows despite the frigid temperature. Its a very bright blue. You also see an old campsite on the western side of the river."
river2: str = "You take your hand out of its glove and test the water. \nYou find that its cold.\nYou continue."
campsite1: str = "You decide to head towards it and forge the river by walking over some rocks. There is somebody at the campsite."
campsite2: str = "The campsite is fairly new, but the coals in the firepit are icy to the touch. \nSome snowed on leftover tents make up the rest of the campsite.\nYou see a swamp bordering the northern side of the campsite and an array of cliffs past it."
swamp1: str = "You eventually find yourself in an ice-covered swamp. Trees sprout from small land masses throughout the swamp."
swamp2: str = "You stop and notice a deer on the far side of the swamp. \nBefore you can move again, it notices you and runs away.\nYou carefully walk over the ice of the swamp."
cliffs1: str = "You find yourself at the base of the cliffs. You look above you and see more cliffs jutting out on top of each other."
cliffs2: str = "A small pathway can be seen clearly carved along the cliffside going north towards the top"
rock1: str = "You make your way to the top of the cliffside and find yourself graced by the presence of a large rock. This is the end. There is somebody you can talk to."
rock2: str = "You take a look around you and decide to take a picture of your surroundings. \nhttps://cdn.discordapp.com/attachments/311944103804010496/1020799631766069331/unknown.png"

pub_NPC: str = "Hello there! The snow is nice outside! I might go up towards the rock on the top of the cliff later today if my work_meeting gets called off early, hahaha! \nI heard my weirdo brothers already went over there."
campsite_NPC: str = "Hello there! You need to go take a shower, BAHAHAHA! \nIf you meet my brother further along this path, say MAYBE to whatever he asks you!"
rock_NPC: str = "Hello there! Did you meet the weird guy at the camp? \nAnswer Carefully...."


class World:
    
    def __init__(self):
        
        ## all areas
        self.areas = [
            locale_1.Locale("Home", home1, home2, False),
            locale_1.Locale("Village", village1, village2, False),
            locale_1.Locale("Pub", pub1, pub2, False),
            locale_1.Locale("Frozen Lake", frozen_lake1, frozen_lake2, False),
            locale_1.Locale("Meadow", meadow1, meadow2, False),
            locale_1.Locale("River", river1, river2, False),
            locale_1.Locale("Campsite", campsite1, campsite2, False),
            locale_1.Locale("Swamp", swamp1, swamp2, False),
            locale_1.Locale("Cliffs", cliffs1, cliffs2, False),
            locale_1.Locale("Rock", rock1, rock2, False)
        ]

        ## area movement matrix
        self.movement_list = [
            [self.areas[0], self.areas[1], self.areas[1], None, None],             # home
            [self.areas[1], self.areas[2], self.areas[3], self.areas[2], None],    # village
            [self.areas[2], None, self.areas[0], None, None],                      # pub
            [self.areas[3], self.areas[0], self.areas[4], None, None],             # frozen_lake
            [self.areas[4], self.areas[3], self.areas[5], None, None],             # meadow
            [self.areas[5], self.areas[4], self.areas[5], None, self.areas[6]],    # river
            [self.areas[6], self.areas[7], None, self.areas[5], None],             # campsite
            [self.areas[7], self.areas[8], self.areas[6], None, None],             # swamp
            [self.areas[8], self.areas[9], self.areas[7], None, None],             # cliffs
            [self.areas[9], None, None, None, None]                                # rock
        ]

        self.npc = [None, None, pub_NPC, None, None, None, campsite_NPC, None, None, rock_NPC]

        self.answers = ["maybe"]

    def get_names(self):
        list_locales = []
        for i in range(0, len(self.areas)):
            list_locales.append(self.areas[i].name)
        return list_locales