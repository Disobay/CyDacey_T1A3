from event_idea import EventIdea

class Event:
    # a list of event ideas
    def __init__(self, event_ideas):
        self.event_ideas = event_ideas

    def print_event(self):
        print("Welcome to Event Planner, this is your Event's for today.:")
        for idea in self.event_ideas:
            idea.show_idea()
    # add a new idea to the list
    def add_idea(self, name, duration):
        new_idea = EventIdea(name, duration)
        self.event_ideas.append(new_idea)

    def delete_idea(self, name):
        # Flow through the list looking for certain event
        for idea in self.event_ideas:
            # check if the events name from the search is equal to the name given
            if idea.name == name:
                # access the list and remove the item
                self.event_ideas.remove(idea)
                return print(f"{name} was removed from the list")
    
        return  print(f"{name} is not in the list")   

    def update_duration(self, name):
        # Search through the list looking for the typed item
        for idea in self.event_ideas:
            # check if the events name from the search is equal to the name given
            if idea.name == name:
                # ask for the new duration
                price = float(input(f"What is the new duration for {name}? "))
                #update the events duration
                idea.duration = duration
                return print(f"{name}'s duration was uptaded in the menu")
    
        return  print(f"{name} is not in the list")   
