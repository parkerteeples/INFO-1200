#!/usr/bin/env python3
print('Parker Teeples Perimeter Program') # print project name

# display a welcome message
print("The Perimeter Program")
print() # print blank

# get inputs from the user
length = int(input('Enter Length:\t'))## get length
width  = int(input('Enter Width:\t'))  ## get width

# calculations
area = length * width ## calculate area
perimeter = (2 * length) + (2 * width) ## calculate the perimeter
            
# format and display the result
print() ## print blank
print("Area =\t\t" + str(area)) ## print area
print('Perimeter =\t' + str(perimeter))## print length
print() ## print blank
print("Bye") ## print bye