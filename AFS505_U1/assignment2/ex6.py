#strings are in double or single quotes, ususally exported in some way
#f-sting f"some stuff {variable}

#assigning variables
types_of_people = 10
x = f"There are {types_of_people} types of people."

#more variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#printing statements
print(x)
print(y)
#printing continued
print(f"I said: {x}")
print(f"I also said: '{y}'")
#setting joke eval variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#printing
print(joke_evaluation.format(hilarious))
#setting variable
w = "This is the left side of ..."
e = "a string with a right side."
#printing combined strings
print(w + e)
