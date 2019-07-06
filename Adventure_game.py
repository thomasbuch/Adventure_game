import time
import random


def print_pause(s):
    print(s)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        choice = input(prompt)
        if choice == option1:
            break
        elif choice == option2:
            break
        else:
            print_pause("Sorry I don't understand")
    return choice


def intro(enemy, inventory):
    print_pause("You find yourself in an open field, filled with grass"
                " and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, and "
                "has been terrifying the nearby village.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave\n\n")
    field(enemy, inventory)


def field(enemy, inventory):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == "1":
        house(enemy, inventory)
    elif choice == "2":
        cave(enemy, inventory)


def house(enemy, inventory):
    print_pause("you approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out"
                f" steps a {enemy}!")
    print_pause(f"Fudge! this is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" in inventory:
        print_pause("You pull out your mighty sword.")
    else:
        print_pause("You feel a bit under-prepared for this, what with only "
                    "having a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == "1":
        if "sword" in inventory:
            print_pause("You are victorious")
            end_of_game()
        else:
            print_pause("You are defeated")
            end_of_game()
    elif choice == "2":
        print_pause("You run back into the field. Luckily, you don't"
                    " seem to have been followed.")
        field(enemy, inventory)


def cave(enemy, inventory):
    print_pause("You peer cautiously into the cave.")
    if "sword" in inventory:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword"
                    " with you.")
        inventory.append("sword")
    print_pause("You walk back into the field.")
    field(enemy, inventory)


def end_of_game():
    print_pause("Would you like to play again?")
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if "1" in choice:
        print_pause("Great!")
        play_game()
    elif "2" in choice:
        print_pause("Thanks for playing!")


def play_game():
    enemy_list = ["gorgon", "dragon", "troll", "witch"]
    inventory = []
    enemy = random.choice(enemy_list)
    intro(enemy, inventory)


play_game()
