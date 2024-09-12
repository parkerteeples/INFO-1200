

secret_word = 'banana' # set value of secret word
guess_word = '' # set value of the guess_word

# while word is not secret word
while guess_word.upper() != secret_word.upper():
    guess_word = input('Guess my secret word, choices are [Banana, Apple, Orange] :') #User input guess
    # Check word to secret word
    if guess_word.upper() == secret_word.upper(): # if matches
        pass # break
    elif guess_word != secret_word: # if doesn't match
        print('Sorry, Try Again') # print "sorry try again"

print('You Won!') # print "You Won!"

# have the user guess the word
# if the user gets the word wrong have them guess again
# if the user gets the word right end game