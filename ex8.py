#! /usr/bin/env python

# Create a formatter variable that contains 4 RAW value display holders.
formatter = "%r %r %r %r"
# Print the python interpretted values which in this case would be real digits 1 2 3 and 4
print formatter % (1, 2, 3, 4)
#print the 4 values inserted into the formatter, which in this case are 4 strings.  the output is has quotes or single quotes to indicate it's a string
print formatter % ("one", "two", "three", "four")
# print the boolean return for the items in the formatter.  True and False are usually determined values or results so they do not have quotes
print formatter % ("True", "False", "False", "True")
# print the raw value for formatter, which is %r %r %r %r as a string
print formatter % (formatter, formatter, formatter, formatter)
# print the string interpretted values inline.  the commas continue the statement.
print formatter % (
    "I had this thing.", 
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

