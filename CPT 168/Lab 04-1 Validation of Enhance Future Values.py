#!/usr/bin/env python3
#Claire Roberson, CPT 168-W18, February 6 2025, Lab 4-1
#This validates the values input by the user

#THIS IS PART 2 OF LAB 04-1. GRADE RECIEVED: 100 / 100

def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number < high:
            valid = True
            return number
        else: 
            print("Must be greater than: ", low, "and less than or equal to: ", high, "Please enter a new number.")

def get_int(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number < high:
            valid = True
            return number
        else: 
            print ("Must be greater than: ", low, "and less than or equal to: ", high, "Please enter a new number.")


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input
        valid_number = get_float("Enter number: ", 0, 1000)
        print("Valid number = ", valid_number)
        print()
        valid_integer = get_int("Enter integer: ", 0, 50)      
        print("Valid integer = ", valid_integer)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()
