#!/usr/bin/env python

# Value definitions, number of cars, the capacity of each car, number of drivers available, number of passengers.
cars = 100
space_in_a_car = 4.0 
drivers = 30 
passengers = 90

# Calculations based on real values, including the number of cars driven and not driven, the total capacity, and the number of passengers in each of the cars driven. 
cars_not_driven = cars - drivers 
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Daily print outs to provide the scheduler (person managing daily opeartions and scheduling) required information to organized carpools.
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
