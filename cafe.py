from os import system
from seed import seed
from list import List

event = seed()


def print_options():
    print("1. Show events for today")
    print("2. Add Event to today's to-do list")
    print("3. Edit the events of the event list")
    print("4. Delete a event from the event list")
    print("5. Make a List")
    print("6. Exit")
    opt = input("Select your option (1-6): ")
    return opt

def delete_events():
    #show the list of events, just names
    for idea in event.event_ideas:
        print(idea.name)
    #ask about the event that would like to be deleted
    name = input("What is the event you want to delete? ")
    event.delete_idea(name)
    #make sure the event is in the list

    #delete it

def add_events():
    name = input("What's the name of the new Event? ")
    price = float(input (f"What's the duration of {name}? "))
    event.add_idea(name, price)
    print(f"{name} being added to the event list...")
    #add a new event with, how long the event will take to finish.

def make_list():
    print("start a new list...")
    #create a new list
    new_list = List()
    cont = "y"
    #add an event to the list, then ask if there are any more events that need to be added
    while cont == "y":
        name = input("What would you like to add to your list?")
        quantity = int(input("How many of them? "))
        new_list.add_idea_to_list(name, quantity)
        cont = input("Anything else? (y/n) ")
    #when all the events are added show the total duration of the list to be completed
    print(new_list.list_ideas)
    print(new_list.calculate_total_bill())

def edit_events():
    event.print_event()
    #ask about the event we want to edit
    name = input("What is the event you want to edit? ")
    #make sure the event is in the list
    event.update_duration(name)
    #ask for the new duration



option = ""

while option != "6":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        event.print_event()
    elif option == "2":
        add_events()
    elif option == "3":
        edit_events()
    elif option == "4":
        delete_events()
    elif option == "5":
        make_list()
    elif option == "6":
        continue
    else:
        print("Invalid option")
        
    input("press Enter to continue")
    system('clear')

print("Goodbye!") 

