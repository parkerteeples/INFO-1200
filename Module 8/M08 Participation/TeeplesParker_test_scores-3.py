#!/usr/bin/env python3

def display_welcome(): # define display_welcome function
    print("The Test Scores program") # print 'The Test Scores program'
    print("Enter 'x' to exit") # print "Enter 'x' to exit"
    print("") # print ""

def get_scores(): # define get_scores function
    scores = [] # set scores as a list
    while True: # while true loop
        score = input("Enter test score: ") # set score as input
        if score == "x": # if score is "x"
            return scores # return scores
        else: # if not x
            score = int(score) # convert score into an intager
            if score >= 0 and score <= 100: # if score is bigger than or equal to 0 and smaller than or equal to 100 
                scores.append(score) # append score or scores list
            else: # else
                print("Test score must be from 0 through 100. " + 
                      "Score discarded. Try again.") # print "Test score must be from 0 through 100. " + "Score discarded. Try again."

def process_scores(scores): # define process_scores function with scores as an argument
    scores.sort() # sorts scores
    # calculate numbers
    score_total = sum(scores) # total
    count = len(scores) # count
    average = score_total / count # average
    low = min(scores) # low score
    high = max(scores) # high score
    median_index = len(scores) // 2 # calculates median index
    if len(scores) % 2 == 0: # if the the lenght of scores % 2 is zero
        median = (scores[median_index] + scores[median_index - 1]) / 2 # set median to the average of the two middle objects in the list
    else: # if not
        median = scores[median_index] # set median to the median_index of scores
                
    # format and display the result
    print() # print blank line
    print("Score total:       ", score_total) # print score_total result
    print("Number of Scores:  ", count) # print count result
    print("Average Score:     ", average) # print average result
    print("Low Scores:        ", low) # low score
    print("High Score:        ", high) # high score
    print("Median Score:      ", median) # median score
def main(): # define main function
    display_welcome() # call display_welcome function
    scores = get_scores() # scores is the results of calling the get_scores function
    process_scores(scores) # call the function process_scores with the list scores as the argument
    print("") # print ""
    print("Bye!") # print "Bye!"

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


