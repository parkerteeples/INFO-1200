print("Parker Teeples Tip Calculator App") ## My Tip Calculator App
print() ## blank line

costOfMeal = float(input("Cost of meal: ")) ## input cost of meal
tipPercentage = float(input("Tip percentage: ")) ## input tip percentage
print() ## blank line

tipAmount = costOfMeal * (tipPercentage / 100) ## calculate tipAmount
tipAmount = round(tipAmount,2) ## round tipAmount to two decimal places
print("Tip amount: " + str(tipAmount)) ## print tip amount

totalAmount = tipAmount + costOfMeal ## totalamount is calculated
totalAmount = round(totalAmount,2) ## totalamount is rounded to two decimal places
print("Total amount: " + str(totalAmount)) ## print total amount
