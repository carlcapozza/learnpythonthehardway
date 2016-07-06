#!/usr/bin/env python

# Using formatters in a string and assign the value to x
x = "There are %d types of people." % 10
# Define some strings to be used later.
binary = "binary"
do_not = "don't"
# Use formatters to insert multiple strings and assign the value to y
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and then print y
print x
print y

# formatter inserts a printable representation of an object.
print "I said: %r." % x
# Formatter inserts the string
print "I also said: '%s'." % y

# defined boolean result.
hilarious = False
# joke evaluation is really a way to pass results to into a string.
joke_evaluation = "Isn't that joke so funny?! %r"

# execute joke evaluation (print the string and pull in the provided answer from another value.
print joke_evaluation % hilarious

# define two strings
w = "This is the left side of ..."
e = "a string with a right side."

# print them in one line using the + operator 
print w + e

