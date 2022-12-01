import world
import locale

class Player:

    def __init__(self, name, p_world):
        self.name = name
        self.p_world = p_world
        self.current_loc = world.areas[0]
        self.stops = 0
        self.score = 0

    def move(self, action):
        
        next_area = self.world.movement_list[action] 
        self.stops += 1

        return next_area, self.stops
        

    def score_counter(self, next_area):

        if next_area.locale.was_visited == False:
            next_area.locale.was_visited = True
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
   