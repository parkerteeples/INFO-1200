#!/usr/bin/env python3

import csv # import cvs

FILE_NAME = 'trips.csv' # file name for file being used

#Write Trips to File
def write_trips(trips): # define write_trips function with the parameter trips
    with open(FILE_NAME,'w',newline='') as output_file: # open file write as output_file
        writer = csv.writer(output_file) # set the writer in the output file
        writer.writerows(trips) # write trips into file

#Read Trips from file
def read_trips(): # define read_trips funciton
    trips = [] # set trips as a list
    with open(FILE_NAME,'r', newline='') as input_file:  # open file as read as output_file
        reader = csv.reader(input_file)  # set the reader in the output file
        for row in reader: # for every row in the file being red
            trips.append(row) # append the result of the row to the list trips
    
    return trips # return trip

def list_trips(trips): # define list_trips with the paramerter trips
    print("Dist\tGallons\tMPG") # print "Distance\tGallons\tMPG"
    # for i in range(0, len(trips)): # for i in range of 0 to length of trips
    #     trip = trips[i] # trips is set to trips i
    #     print(str(trip[0]) + '\t' + str(trip[1]) + '\t' + str(trip[2])) # print trips 0, 1, and 2
    for trip in trips: # for trip in trips
        print(f"{str(trip[0])}\t{str(trip[1])}\t{str(trip[2])}") # print trip 0, 1, 2
    print() # print blank line

def get_miles_driven(): # define get_miles_driven function
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0: # while miles_driven is the input set asa a float bigger than zero           
        print("Entry must be greater than zero. Please try again.\n") # print "Entry must be greater than zero. Please try again.\n"    
    return miles_driven # return miles driven
          
def get_gallons_used(): # define get_gallons_used function
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0: # while miles_driven is the input set asa a float bigger than zero    
        print("Entry must be greater than zero. Please try again.\n") # print "Entry must be greater than zero. Please try again.\n"
    return gallons_used # return gallons used

def main(): # define main function
    # display a welcome message
    print("The Miles Per Gallon program") # print "The Miles Per Gallon program"
    print() # print blank line

    trips = read_trips() # set trips to result of read_trips
    list_trips(trips) # call list_trips with trips as argument

    more = "y" # set more to 'y'
    while more.lower() == "y": # while more in lowercase is 'y'
        miles_driven = get_miles_driven() # set miles_driven to the result of calling the funciton get_miles_driven
        gallons_used = get_gallons_used() # set gallon_used to the result of calling the funciton get_gallon_used
        
        mpg = round((miles_driven / gallons_used), 2) # set mpg to miles_driven / gallons used rounded by 2

        trips.append([miles_driven, gallons_used, mpg]) # add miles_driven, gallons_used, mpg to the list trips

        print(f"Miles Per Gallon:\t{mpg}") # print "Miles Per Gallon:\t{mpg}"
        print() # print blank line
        
        more = input("More entries? (y or n): ") # get the input and store it in more

    write_trips(trips) # call the function write_trips with the argument trips
    list_trips(trips) # call the function list_trips with the argument trips
    
    print("Bye!") # print "Bye!"

if __name__ == "__main__": # if name is main
    main() # call main

