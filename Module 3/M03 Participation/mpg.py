#!/usr/bin/env python3
print('Parker Teeples MPG APP')
print()

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t")) 
gallon_cost  = float(input('Enter cost per gallon:\t\t')) # get cost per gallon from the user

# Do calculations
mpg = round(miles_driven / gallons_used, 1) # calculate mpg
gas_cost = round(gallons_used * gallon_cost , 1) # calculate cost of gas
mile_cost = round(gas_cost / miles_driven , 1) # calculate cost per mile            

# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg)) # print mpg
print("Total Gas Cost: \t\t" + str(gas_cost)) # print total cost of gas
print("Cost Per Mile: \t\t\t" + str(mile_cost)) # print cost per mile
print() # print blank
print("Bye") # print bye


