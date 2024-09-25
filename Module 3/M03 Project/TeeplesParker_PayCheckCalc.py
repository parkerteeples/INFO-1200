print("Parker Teeples Pay Check Calculator App") ## my Pay Check Calculator App
print() ## blank line

hoursWorked = float(input("Hours Worked: ")) ## input hours worked
payRate = float(input("Hourly Pay Rate: ")) ## input hourly pay rate
print() ## blank line

grossPay = hoursWorked * payRate ## gross pay is hoursworked multiplied by pay rate
print("Gross Pay: " + str(grossPay)) ## print gross pay and variable grosspay


taxRate = float(.18) ## the variable taxRate is given .18
print("Tax Rate: " + str(taxRate * 100) + "%") ## print tax rate

taxAmount = grossPay * (taxRate) ## calculates tax amount
print("Tax Amount: " + str(taxAmount)) ## print tax amount

takeHomePay = grossPay - taxAmount ## calculate take home pay
takeHomePay = round(takeHomePay,2) ## round take home pay by two decimal places
print("Take Home Pay: " + str(takeHomePay)) ## prints take home pay