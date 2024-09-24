# print("Hello world")
# input("Enter Your Name")

# var1 = 2.4546

# round(var1,2)
# round(35.23463,3)

# float()
# int()
# str()



# function that prints a welcom message (no arguments)
# def print_welcome():
#     print('-------------------------')
#     print("Welcome to My Application")
#     print('-------------------------')

# print_welcome() 
# print_welcome()

# Welcome message with argument
# def print_welcome(custom_message):
#     print('-------------------------')
#     print("Welcome to My Application")
#     print()
#     print(custom_message)
#     print('-------------------------')

# print_welcome("Today is a great day!")
# print_welcome("It's great to see you again!")
# print_welcome()

# function with 2 arguments
def calculate_mpg(miles, gallons):
    mpg = miles / gallons
    mpg = round(mpg,1)
    print("Your mpg is " + str(mpg))

def main():
    miles_driven = 45
    gallons_used = 2.1
    calculate_mpg(miles_driven, gallons_used)
    calculate_mpg(gallons=gallons_used, miles=miles_driven)

# if __name__ == "__main__":
#     main()
    
## Function with a defualt value
def calc_investments(monthly_investment=100,years=30,yearly_interest=7.42):
    monthly_interest_rate = yearly_interest/12/100
    months = years*12
    future_value = 0
    for i in range (0,months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return round(future_value,2)

total_investments = calc_investments(200,20)
print(total_investments)

total_investments = calc_investments(200,20,10)
print(total_investments)

total_investments = calc_investments(200)
print(total_investments)

print("hello",end=" ")
print("world")