from world import *
from locale_1 import *

class Player:

    def __init__(self, name, p_world):
        self.name = name
        self.p_world = p_world
        self.current_loc = p_world.areas[0]
        self.stops = 0
        self.score = 0

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
            print(new_loc)
            self.current_loc,self.score = self.score_counter(new_loc, self.score)
    
    def examine(self,current_loc):

        print(current_loc.details)
            
   