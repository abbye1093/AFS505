people = 20
cats = 30
dogs = 15
# if statements, test the statement given and follow the outcome underneath the statement
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")
# add 5 to dogs before the rest of the tests
dogs += 5
# dogs is equal to people now so all three of these will print
if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
