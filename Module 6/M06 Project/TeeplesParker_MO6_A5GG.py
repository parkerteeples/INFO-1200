50#!/usr/bin/env python3

import random # imports the random module

def display_title(): # define the display_title function
    print("Guess the number!") # print "Guess the number!"
    print() # print blank line

def get_limit(): # define the get_limit function
    limit = int(input("Enter the upper limit for the range of numbers: ")) # get the input for limit
    return limit # return limit

def play_game(limit): # define the function for play_game
    number = random.randint(1, limit) # number is set to a random int between 1 and limit
    print(f"I'm thinking of a number from 1 to {limit}\n") # print "I'm thinking of a number from 1 to {limit}
    count = 1 # set count to 1

    while True: # while true
        guess = int(input("Your guess: ")) # input guess
        if guess < number: # if guess is less than number
            print("Too low.") # print "Too low."
            count += 1 # add 1 to count
        elif guess > number: # if guess is bigger than number
            print("Too high.") # print "Too high."
            count += 1 # add one to count
        elif guess == number: # if guess is number
            print(f"You guessed it in {count} tries.\n") # print "You guessed it in {count} tries.'
            return # return

def main(): # define the function main
    display_title() # call the display_title function
    
    again = "y" # set again to 'y'
    while again.lower() == "y": # while again is 'y'
        limit = get_limit() # set limit to the result of the get_limit function
        play_game(limit) # call the play_game function with the argument of limit
        
        again = input("Play again? (y/n): ") # get input for again
        print() # print blank line
    print("Bye!") # print 'Bye!'

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

