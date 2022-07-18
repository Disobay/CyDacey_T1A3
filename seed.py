from event_idea import EventIdea
from event import Event
# seed the Menu put of the main file
def seed():
    eventt1 = EventIdea("Grocery Shopping", 30)
    eventt2 = EventIdea("Go to the Gym", 75)
    eventt3 = EventIdea("Play my favourite video game", 120)
    eventt4 = EventIdea("Spend time with the family", 180)
    event = Event([eventt1, eventt2, eventt3, eventt4])
    return event