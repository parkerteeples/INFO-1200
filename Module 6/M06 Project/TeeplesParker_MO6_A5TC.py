#!/usr/bin/env python3

tax = 0.06 # assaign tax percentage to the variable

def sales_tax(total): # define function for sales_tax with the argument 'total'
    sales_tax = total * tax # caluculate sales_tax
    return sales_tax # return sales_tax

def main(): # define the main function
    print("Sales Tax Calculator\n") # print name of program
    total = float(input("Enter total: ")) # input amount for total
    total_after_tax = round(total + sales_tax(total), 2) # using the function sales_tax, calculate total after tax and round
    print("Total after tax: ", total_after_tax) # print result
    
if __name__ == "__main__": # if name is main
    main() # call main
