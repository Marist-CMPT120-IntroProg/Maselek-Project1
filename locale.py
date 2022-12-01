class Location: 

    def __init__(self,name, summary, details, was_visited = False):
        self.name = name
        self.summary = summary
        self.details = details
        self.was_visited = was_visited

    def __str__(self):
        if self.was_visited == True:
            current_loc = ("You are at " + self.name)

        elif self.was_visited == False:
            self.was_visited == True
            current_loc = self.summary
        return current_loc

    def was_visited_manual(self):
        self.was_visited = True

    def show_details(self):
        print()
        print(self.details)
