#!/usr/bin/env python3
#Claire Roberson, January 30 2025, Lab 03-1, CPT 168-W18



# display a welcome message
print("The Miles Per Gallon program")
print()

#Repeats while the user inputs y for choice
choice = 'y'
while choice == 'y':
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    #gets the cost of 1 gallon of gas for the calculation of 
    cost_per_mile = float(input('Enter cost of 1 gallon of gas:     '))  
    
#Checks to make sure the user isn't inputting 0 for the multiplication to work 
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.") 
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.") 
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)
        cost = round(mpg * cost_per_mile, 2)
        print('Cost of trip:    ', cost)
    #Asks the user if they want to calculate another trip
    choice = input('Get entries for another trip? (y/n)')


print()
print("Bye!")



