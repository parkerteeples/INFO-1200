#!/usr/bin/env python3

# display a welcome message
print("Parker's Miles Per Gallon application")
print()

another_trip = 'y'

while another_trip.lower() == 'y':
    # get input from the user
    miles_driven    = float(input("Enter miles driven:          "))
    gallons_used    = float(input("Enter gallons of gas used:   "))
    cost_per_gallon = float(input("Enter cost per gallon:       "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2) # calculate mpg
        total_cost = (gallons_used * cost_per_gallon) # calculate total cost
        cost_per_mile = (total_cost / miles_driven) # calculate cost per mile
        print()
        print("Miles Per Gallon:           ", mpg) # print out the mpg
        print("Total Cost:                 ", round(total_cost,2)) # print out the total cost
        print("Cost Per Mile:              ", round(cost_per_mile,2)) # print out the cost per mile
        print()
        another_trip = input("Do you want to enter another trip? (y/n) : ") # ask user if they want to input another trip
        print()
    
print("Bye") # print Bye



