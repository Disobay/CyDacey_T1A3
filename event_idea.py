class EventIdea:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show_idea(self):
        print(f"{self.name}: Minutes Taken :{self.duration}")
