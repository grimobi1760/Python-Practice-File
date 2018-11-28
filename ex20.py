from sys import argv
script, input_file = argv
#define a function that would read the input_file
def print_all(f):
    print(f.read())
#start over the input_file
def rewind(f):
    f.seek(0)
#print out the line of the input file
def print_a_line(line_count, f):
    print(line_count, f.readline())
#open the input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines: ")
#iterate accross the line within the input_file
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
