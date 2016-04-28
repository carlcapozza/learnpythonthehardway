#! /usr/bin/env python

name = 'Zed A. Shaw' 
age = 35 # not a lie
height_in_in = 74.0 # inches 
height_in_cm = height_in_in * 2.54 # cm
weight_in_lbs = 180.0 # lbs 
weight_in_kg = ( 1 / 2.2 ) * weight_in_lbs # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_in_in
print "That's %r centimeters." % height_in_cm
print "He's %d pounds heavy." % weight_in_lbs
print "That's %r kilograms." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
   age, height_in_in, weight_in_lbs, age + height_in_in + weight_in_lbs)


