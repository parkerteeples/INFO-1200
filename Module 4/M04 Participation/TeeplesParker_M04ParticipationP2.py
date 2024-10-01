#!/usr/bin/env python3


def get_input(input_type, max_value):
    is_valid = False
    while not is_valid:
        # get input from the user
        user_value = float(input("Enter " + input_type + ":\t"))
        if user_value >= 0 and user_value <= max_value:
            is_valid = True
        else:
            print(input_type + " must be greater than 0 and no more than "+ str(max_value))
    
    return user_value

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
number = 50
# will loop when choice is y
while choice.lower() == "y":
    
    monthly_investment   = get_input("monthly investment", 1000)
    yearly_interest_rate = get_input("Yearly interest rate", 15)
    years = get_input('Number of years', 50)

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = int(years) * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        if i % 12 == 0 and i !=0:
            print("Year = ", (i // 12), "\tFuture Value = ", round(future_value, 2))

        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount


    # display the result
    print("Year = " + years+ "\tFuture value = ", round(future_value, 2))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
