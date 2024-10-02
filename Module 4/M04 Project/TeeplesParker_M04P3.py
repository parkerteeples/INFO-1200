#Name: (Parker Teeples)
#Class: (INFO 1200)
#Section: (X01)
#Professor: Tyler Bartholomew
#Date: 10/1/2024
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Parker Teeple's Change App") # print name of code
print() # print blank line

choice = 'y' # give the variable choice 'y'
while choice.lower() == 'y': # while choice is y it will loop
    cents = int(input("Enter number of cents(0-99): ")) # input for the number of cents stored in cents
    print() # blank line
    quarters = cents // 25 # calculate amount of quaters needed
    cents = cents % 25 # find remainding after removing quaters
    dimes = cents // 10 # calculate amount of dimes
    cents = cents % 10 # find remainder after removing dimes
    nickles = cents // 5 # calculate amount of nickles
    cents = cents % 5 # find remainder after removing nickles
    pennies = cents # pennies are the remaining abount
    print("Quaters:", quarters) # print quaters
    print("Dimes:  ", dimes) # print dimes
    print("Nickles:", nickles) # print nickles
    print("Pennies:", pennies) # print pennies
    print() # blank line
    choice = input("Continue? (y/n): ") # get input if they want to continue
    print() # blank line
print("Bye!") # print bye
