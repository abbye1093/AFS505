# defining the functions that will later be used to do math things
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
#return sets variables to be values from a function
#add a and b and then return them
#****the result is assigned to a variable**** < new and exciting part
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")
# defining the var and calling the above functions to complete the math?
age = add(30, 5)
#since our functions use return to assign a variable, the addtion happens and then age = the result
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
#return allows the next line to happen, since all the answers to the math have been assigned to variables
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
