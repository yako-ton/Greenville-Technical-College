#!/usr/bin/env python3

#Claire Roberson, January 30 2025, Lab 03-2, CPT 168-W18
#This code calculates the average of test scores from user input, and will repeat if user types 'y'

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 999 to end input")
print("======================")


#starts the loop again if user inputs y at the end
repeat = 'y'
while repeat == 'y':
    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    #this checks to see if the user has put in the number to end the program or not, 999, which is not a valid test score
    while test_score != 999:
        #input is a float in case test score has a decimal
        test_score = float(input("Enter test score: "))
        #checks to make sure test score is between 0 and 200. Goes above 100 in case of extra credit
        if test_score >= 0 and test_score <= 200:
            score_total += test_score
            counter += 1
        elif test_score == 999:
            break
        else:
            print(f"Test score must be from 0 through 200. "
                  f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    
    #asks the user if they want to calculate another average and repeat the code
    repeat = input('Enter another set of test scores? (y/n)')


#ending message
print()
print("Bye!")


