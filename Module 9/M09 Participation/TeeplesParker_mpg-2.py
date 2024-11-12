#!/usr/bin/env python3

import csv

FILE_NAME = 'trips2.csv'

#Write Trips to File
def write_trips(trips):
    with open(FILE_NAME,'w',newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(trips)

#Read Trips from file
def read_trips():
    trips = []
    with open(FILE_NAME,'r', newline='') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            trips.append(row)
    
    return trips

def list_trips(trips):
    print("Distance\tGallons\tMPG")
    for i in range(0, len(trips)):
        trip = trips[i]
        print(trip[0] + '\t' + trip[1] + '\t' + trip[2])
    print()

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

