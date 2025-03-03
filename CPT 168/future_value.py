#!/usr/bin/env python3
#Claire Roberson, CPT 168-W18, February 6 2025, Lab 4-1

#This program calculates the future values from user input, while validating the input from a seperate module


#imports the module "validation" and assigns it to keyword v
import validation as v

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user using the functions defined from the validation module, v.FUNCTION, with validation criteria at end of input
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        # displays the future value rounded to 2nd decimal place
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
