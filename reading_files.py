from sys import argv

# Establishing variables
script, filename = argv

# Open filename, called below
txt = open(filename)

# Print the string with filename
print "Here's your file %r:" % filename

# Print the content of called filename
print txt.read()

# Input filename again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open (file_again)

# Print the content of the called file again
print txt_again.read()