#reading and writing files
#close: closes the file, similar to file > save
#read: reads contents of files
#readline: reads just one readline
#truncate: empties the file
#write('stuff') : writes 'stuff' to file
#seek(0): moves the read/write location to the beginning of the files

from sys import argv

script, filename = argv
#getting filename from the argv entry when opening/running py file
print(f"We're goint to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") #want input from user while script is running

print("Opening the file...")
target = open(filename, 'w') #opening the file in write mode, instead of default read

print("Truncating the file. Goodbye!")
#truncating empties the file
target.truncate()

print("Now I'm going to ask you for three lines.")
#asks for user input for each line
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#will this work? nope,
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally, we close it.")
#close aka file > save
target.close() #run close with no parameter changes on target
