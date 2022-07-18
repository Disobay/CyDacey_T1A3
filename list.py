class List:
    def __init__(self):
        self.list_ideas = {}


    # Add an event to the list
    def add_idea_to_list(self, name, quantity):
        # search if the name is in the dictionary
        if name in self.list_ideas:
            # if the name already is in the dictionary, let's decide the amount of time's this event needs to be done
            self.list_ideas[name] += quantity
        else: 
            # if the name is not in the dictionary, let's assign how many times the event should be carried out
            self.list_ideas[name] = quantity


    def calculate_total_bill(self):
        total = 0
        for name, quantity in self.list_ideas.items():
            duration = 5 
            total += duration * quantity
        return f"Total bill: ${total}"