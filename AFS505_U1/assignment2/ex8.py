#printing, printing
#define formatter function
formatter = "{} {} {} {}"
#when calling formatter, apply this format to the next 4 items
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#replace the four items with the following: 
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

#using a function to turn the formatter variable into a string
