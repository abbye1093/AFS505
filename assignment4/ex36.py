from sys import exit

def start():
    print("You are in a dark room.")
    print("There is a door to your right and your left.")
    print("Which do you take?")
    choice = input("> ")

    if choice == "left":
        library()
    elif choice == "right":
        bedroom()
    else:
        dead("You stumble around the room until you starve.")


def library():
    print("You enter a room full of books.")
    print("Do you look at the books, or look for an exit?")
    choice = input("> ")

    if choice == "look at books":
        print("You find a mysterious spellbook.")
        print("Do you read it?")
        choice = input("> ")

        if choice == "yes":
            print("The spell transforms you into a dragon.")
            dead("Enjoy your new form!")
        elif choice == "no":
            print("You're right, magic is dangerous.")
            dead("Who knows what may have happened to you!")
        else:
            dead("You take too long to decide and the book disappears.")

    elif choice == "look for exit":
        print("You find a hidden door.")
        print("Do you enter?")
        choice = input("> ")

        if choice == "yes":
            candy_stash()
        elif choice == "no":
            dead("You take too long to decide and turn to dust.")
        else:
            print("Choose yes or no!")
    else:
        print("Choose 'look at books' or 'look for exit'.")

def bedroom():
    print("You enter a lavishly decorated bedroom.")
    print("There is a large wardrobe across from you.")
    print("It begins to shake.")
    print("Do you run or stay and fight?")
    choice = input("> ")

    if choice == "run":
        print("You leave the bedroom.")
        start()
    elif choice == "fight":
        print("You pull out your sword (you have a sword?!)")
        print("The wardrobe opens its doors to reveal a huge mouth!")
        print("Do you run or stab?!")
        choice = input("> ")

        if choice == "run":
            print("You leave the bedroom.")
            start()
        elif choice == "stab":
            print("You pierce its body and it shrivels to nothing.")
            print("A secret exit is revealed.")
            candy_stash()
        else:
            dead("You take too long to react and the wardrobe eats you.")
    else:
        dead("You take too long to react and the wardrobe eats you.")

def candy_stash():
    print("You enter a room that appears to be filled with... candy!")
    print("I wonder who left all of this here...")
    dead("Don't eat too much!")

def dead(why):
    print(why, "Goodbye!")
    exit(0)


start()
