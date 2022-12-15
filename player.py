from world import *
from locale_1 import *

class Player:

    

    def __init__(self, name, p_world):
        self.name = name
        self.p_world = p_world
        self.current_loc = p_world.areas[0]
        self.stops = 0
        self.score = 0
        self.gameover = 0

    def move(self, action):
        
        next_area = self.p_world.movement_list[self.p_world.areas.index(self.current_loc)][action] 
        self.stops += 1

        return next_area, self.stops
        

    def score_counter(self, next_area, score):

        if next_area.was_visited == False:
            next_area.was_visited = True
            self.score += 10
                            
        current_loc = next_area

        return current_loc, self.score

    def move_check(self, action):

        new_loc, self.stops = self.move(action)
        if new_loc == None:
            print("")
            print("")
            print("You can't go that way.")
        
        else:
            print("")
            print("")
            print(new_loc)
            self.current_loc, self.score = self.score_counter(new_loc, self.score)

    def talk(self):


        if self.p_world.npc[self.p_world.areas.index(self.current_loc)] == rock_NPC:
            print("")
            print("")
            print(rock_NPC)
            print("")
            answer = input("What did he tell you?")
            if answer.lower() in self.p_world.answers:
                print("")
                print("")
                print("GRAHHAHA!!! You did meet him.")
                self.score = 1000
                self.gameover = 1
            else:
                print("")
                print("")
                print("You did not meet him? Shame. \n*He takes a sword out and runs you back to Home!*")
                self.gameover = 2
                
    
        elif self.p_world.npc[self.p_world.areas.index(self.current_loc)] == None:
            print("")
            print("Looks like there isn't anyone to talk to.")

        
        else:
            print("")
            print("")
            print(self.p_world.npc[self.p_world.areas.index(self.current_loc)])

    
    def details(self,current_loc):

        print(current_loc.details)
            
   