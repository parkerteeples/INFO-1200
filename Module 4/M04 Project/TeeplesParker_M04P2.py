#Name: (Parker Teeples)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Tyler Bartholomew)
#Date: 10/1/2024
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Parker Teeple's Tip Calculator") # print name of assignment
print() # blank line

meal_cost = int(input("Cost of meal: ")) # input the cost of the meal to meal_cost variable
print() # blank line
for tip_percent in range(15, 30, 5): # loops three times for the values 15 20 and 25
    print(str(tip_percent) + "%")
    tip_percent = int(tip_percent)/100 # turn tip percent into a decimal
    tip_amount = tip_percent * meal_cost # calculate tip amount
    total = tip_amount + meal_cost # calculate the total
    round(total, 2) # round total to two decimal places
    print("Tip amount:", tip_amount) # print tip amount
    print("Total amount:", total) # print total
    print() # print blank line