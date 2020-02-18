from sys import argv

script, input_file = argv
# defining print_all function, apply .read to the function
def print_all(f):
    print(f.read())
# defining the rewind function, apply .seek to the function, seek line 0 or the beginning?
def rewind(f):
    f.seek(0)
# define print_a_line function, print the line number and read line by line with .readline
def print_a_line(line_count, f):
    print(line_count, f.readline())
# open the input file and name as an object current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# go back to first line of file, rewind is defined in line 8
rewind(current_file)

print("Let's print three lines:")
# start at first line, use function print_a_line on current_line in current_file
current_line = 1
print_a_line(current_line, current_file)
# repeat, advancing to line 2
current_line = current_line += 1
print_a_line(current_line, current_file)
# repeat, advancing to line 3
current_line = current_line +=
print_a_line(current_line, current_file)
