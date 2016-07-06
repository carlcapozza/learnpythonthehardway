#!/usr/bin/python

from sys import argv

script, filename = argv

print "we are going to erase %r." % filename 
print "if you don't want that, hit CRTL-C (^C)."
print "if you do want that, hit RETURN"

raw_input("?")

print "openning the file...."
target = open(filename, 'w')

print "truncating the file. Goodbye!"
target.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close the file"
target.close()


 
