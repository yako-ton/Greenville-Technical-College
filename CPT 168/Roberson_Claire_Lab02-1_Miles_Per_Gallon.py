#!/usr/bin/env python3
#Claire Roberson, January 25 2025, Lab 02-1
#This program calculates the miles per gallon and cost per mile based off of user input


# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))

#asks for cost of a gallon of gas
cost_of_gallon = float(input("Enter cost of 1 gallon of gas:\t\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)

#calculates the cost per mile
cost_per_mile = mpg / cost_of_gallon
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Cost Per Mile:\t\t{cost_per_mile}")
print("Bye!")


