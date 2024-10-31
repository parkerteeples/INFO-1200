#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Sharp)
#Date:
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.
import ptconverter as c

print("Parker Teeples Feet / Meters Converter") # print project name
print() # print blank line

def fm_welcome(): # define fm_welcome function
    print("Parker Teeples Feet and Meters Converter") # name of program

def fm_menu(): # define fm_menu function
    print("Conversions Menu:") # print menu title
    print("a. Feet to Meters") # print option a
    print("b. Meters to Feet") # print option b

def main(): # define main function
    fm_welcome() # call fm_welcome
    while True: # while true loop
        fm_menu() # call fm_menue
        choice = input("Select a conversion (a/b):") # select option a or b in choice
        print() # print blank line
        if choice.lower() == 'a': # if choice is a
            feet = float(input("Enter feet:")) # input feet
            meters = c.to_meters(feet) # convert to meters
            print(round(meters, 2), "meters") # print results
        elif choice.lower() == 'b': # if choice is b
            meters = float(input("Enter meters:")) # input meters
            feet = c.to_feet(meters) # convert to feet
            print(round(feet, 2), "feet") # print results
        else: # If not a or b
            print("You did not enter a valid selection") # print non valid selection
        more = input("Would you like to perform another conversion? (y/n):") # input for doing again
        print() # print blank line
        if more != 'y': # if more is not y
            print("Thanks, bye!") # print bye
            break # break while loop
print() # print blank line
if __name__ == "__main__": # if name is main 
    main() # call main
