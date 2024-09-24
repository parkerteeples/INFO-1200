# GLOBAL CONSTANTS
TAX = .25

def calc_tax(amount):
    return amount + amount * TAX

amount = float(input("enter amount: "))
print("tax rate is: " + str(TAX))
amount_plus_tax = calc_tax(amount)
print("Amount plus tax is: " + str(amount_plus_tax))