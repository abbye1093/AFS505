people = 45
cars = 40
trucks = 25

# first the if statement is tested, if TRUE, print statements
if cars > people:
    print("We should take the cars.")
# next the else if statement is tested, if TRUE, print first option, if FALSE follow else branch
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
