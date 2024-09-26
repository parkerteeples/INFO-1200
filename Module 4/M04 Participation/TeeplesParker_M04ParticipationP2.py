#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
number = 50
# will loop when choice is y
while choice.lower() == "y":
    # get monthly investment from user and check is matches requirments. If not loop and have them try again
    is_valid = False
    while not is_valid:
        # get input from the user
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment >= 0 and monthly_investment <= 1000:
            is_valid = True
        else:
            print("Monthly Investment must be greater than 0 and no more than $1000")

    # get yearly interest rate from user and check is matches requirments. If not loop and have them try again
    is_valid = False
    while not is_valid:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            is_valid = True
        else:
            print("Yearly interest rate must be greater than 0 and no more than 15")

    # get number of years from user and check is matches requirments. If not loop and have them try again
    is_valid = False
    while not is_valid:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            is_valid = True
        else:
            print("Number of years must be greater than 0 and no more than 50")

    is_valid = False

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        if i % 12 == 0 and i !=0:
            print("Year = ", (i // 12), "\tFuture Value = ", round(future_value, 2))

        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount


    # display the result
    print("Year =  12\tFuture value = ", round(future_value, 2))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
