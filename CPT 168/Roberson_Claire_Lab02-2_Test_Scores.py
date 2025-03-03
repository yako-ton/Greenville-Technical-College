#!/usr/bin/env python3
#Claire Roberson, January 25 2025, Lab 02-2, CPT 168-W18
#This calculatues the average for 3 test scores entered by the user

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
first_score = int(input("Enter first test score: "))
second_score = int(input("Enter second test score: "))
third_score = int(input("Enter third test score: "))

#adds each score to make a total score for the average_score calculation
total_score = first_score + second_score + third_score

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
#prints each score entered by the user
print("First Test Score: ", first_score,
      "\nSecond Test Score: ", second_score,
      "\nThird Test Score: ", third_score)
print()

#prints the total and average score based on user input      
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye!")


