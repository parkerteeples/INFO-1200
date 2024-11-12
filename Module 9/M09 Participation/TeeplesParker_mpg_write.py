#!/usr/bin/env python3

import csv # import csv

FILE_NAME = 'trips.csv' # file name for file being used

def get_miles_driven(): # define get_miles_driven function
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0: # while miles_driven that is being set to float of input is smaller or equal to zero
        print("Entry must be greater than zero. Please try again.\n") # print "Entry must be greater than zero. Please try again.\n"
    return miles_driven # return miles driven
          
def get_gallons_used(): # define get_gallons_used function
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0: # while gallons used that is being set to float of input is smaller or equal to zero
        print("Entry must be greater than zero. Please try again.\n") # print "Entry must be greater than zero. Please try again.\n"
    return gallons_used # return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()
    
    # Create list
    trips = [] 

    # add Items to list
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        trips.append([miles_driven, gallons_used, mpg])

        more = input("More entries? (y or n): ")
    
    # Send list to file
    with open(FILE_NAME,'w',newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(trips)

    print("Bye!")

if __name__ == "__main__":
    main()

