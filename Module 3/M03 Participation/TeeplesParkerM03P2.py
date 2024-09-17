#!/usr/bin/env python3
print('Parker Teeples Test Results')

# display a welcome message
print("The Test Scores program")
print() ## print blank
print("Enter 3 test scores") # prompt user to enter test scores
print("======================") #formating

# get scores from the user

score1 = int(input("Enter test score: ")) # get score 1
score2 = int(input("Enter test score: ")) # get score 2
score3 = int(input("Enter test score: ")) # get score 3

total_score = score1 + score2 + score3 # add 3 scores to total score

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================") # formating
print('Your scores: ' + str(score1) + ' ' + str(score2) + ' ' + str(score3))# print all 3 scores
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score) # prints total score and average score
print() # print blank
print("Bye") # print bye


