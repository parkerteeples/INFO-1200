#!/usr/bin/env python3
        
def get_number(prompt, low, high): # define the get_number function with prompt, low, high as parameters
    while True: # while true
        try: # try following
            number = float(input(prompt)) # number is the float of user input with the parameter prompt
            if number > low and number <= high: return number # if number is bigger than low and lower or equal to high: return number
            else: print(f"Entry must be greater than {low} and less than or equal to {high}.") # else print "Entry must be greater than {low} and less than or equal to {high}."
        except ValueError: print("value was not a number, try again") # except if ValueError: print "value was not a number, try again"
            
def get_integer(prompt, low, high): # define the get_integer function with prompt, low, high as parameters
    while True: # while true
        try: # try follwing
            number = int(input(prompt)) # number is set to the int of user input with the parameter prompt
            if number > low and number <= high: # if number is bigger than low and lower or equal to high
                return number # return number
            else: # else
                print(f"Entry must be greater than {low} " # print "Entry must be greater than {low} "
                    f"and less than or equal to {high}.") # print "and less than or equal to {high}."
        except ValueError: # if value error
            print("Number was not an integer, Try again") # print "Number was not an integer, Try again"


def calculate_future_value(monthly_investment, yearly_interest, years): # define the calculate_future_value function with the parameters monthly_investment, yearly_interest, years
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 # monthly_intrest_rate is set to yearly_interest / 12 / 100
    months = years * 12 # set months to years * 12

    # calculate future value
    future_value = 0.0 # future_value is set to 0
    for i in range(months): # for i in range of months
        future_value += monthly_investment # future_value is set to itself plus monthly_investment
        monthly_interest = future_value * monthly_interest_rate # monthly_interest is set to future_value * monthly_interest_rate
        future_value += monthly_interest # future_value is set to itself plus monthly_interest

    return future_value # return future_values

def main(): # define main
    choice = "y" # choice is set to 'y'
    while choice.lower() == "y": # while the lower case of choice is 'y'
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000) # call get_number with the arguments "Enter monthly investment:\t", 0, 1000 and set it to monthly investment
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15) # call get number with the arguments "Enter yearly interest rate:\t", 0, 15 and set it to yearly intrest rate
        years = get_integer("Enter number of years:\t\t", 0, 50) # call get_integer with the arguments "Enter yearly interest rate:\t", 0, 15

        # get and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years) # call the function calculate_future_value with the arguments monthly_investment, yearly_interest_rate, years and the result is set to future_value
        
        print() # print blank line
        print(f"Future value:\t\t\t{round(future_value, 2)}") # print "Future value:\t\t\t{round(future_value, 2)}
        print() # print blank line

        # see if the user wants to continue
        choice = input("Continue? (y/n): ") # set choice to the input of the user
        print() # print blank line

    print("Bye!") # print "Bye!"
    
if __name__ == "__main__": # if name is main
    main() # call main
