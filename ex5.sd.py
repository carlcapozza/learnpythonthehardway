#! /usr/bin/env python

name = 'Zed A. Shaw' 
age = 35 # not a lie
height_in_inches = 74 # inches 
weight_in_lbs = 180 # lbs 
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_in_inches
print "He's %d pounds heavy." % weight_in_lbs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
   age, height_in_inches, weight_in_lbs, age + height_in_inches + weight_in_lb)


