#reading files

from sys import argv
#get agrv
script, filename = argv

txt = open(filename)
#using new command 'open'
# checked pydoc open to see details of command
# does NOT return the content of the file, it makes a file object

print(f"Here's your file {filename}:")
#message to user
print(txt.read())
#call a function called read
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
