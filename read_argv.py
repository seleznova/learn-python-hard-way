from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening file..."
target = open (filename, 'w')

print "Truncating the file. Goodbye!"

target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm going to write these to the file."
m = "line1" + "\n" + line2 + "\n" + line3 + "\n"
target.write(m)

print "And finally, we close it."

target.close()