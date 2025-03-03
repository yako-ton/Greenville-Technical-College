#!/usr/bin/env python3
#Claire Roberson, CPT 168-W18, February 11 2025, Lab 5-1
#This program calculates the averages of test scores the user puts in until they input x to quit the program. The program was given to us with an extra counter+=1 which incorrectly calculated the averages.

#GRADE RECIEVED: 100 / 100


# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = float(test_score)
        counter += 1
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        #Removed a counter+=1 here because it already added one to the counter by checking if the user didn't enter x. 
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print("Bye")


