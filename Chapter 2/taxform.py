# Chapter 2, Project 1. 
# Use the round function to modify the tax calculator program to display at most two digits of precision in the output number.

"""
Program: taxform.py
Author: Ken Lambert
Compute a person's income tax.
Significant constants
       tax rate
       standard deduction
       deduction per dependent
The inputs are
       gross income
       number of dependents
Computations:
       net income = gross income - the standard deduction - a deduction for each dependent
       income tax = is a fixed percentage of the net income
The output is
       the income tax
"""

# Initialize the constants
tax_rate = 0.20
standard_deduction = 10000.0
dependent_deduction = 3000.0

# Define each input
gross_income = float(input("Enter the taxpayer's gross income: "))
number_dependents = int(input("Enter the number of taxpayer dependents: "))

# Compute the income tax
taxable_income = gross_income - standard_deduction - \
                dependent_deduction * number_dependents
income_tax = taxable_income * tax_rate

x=round(income_tax,2)

# Display the income tax
print("The taxpayer's income tax is $" + str(x))





Answer:

Enter the taxpayer's gross income: 
50000
Enter the number of taxpayer dependents: 
3
The taxpayer's income tax is $6200.0


** Process exited - Return Code: 0 **
Press Enter to exit terminal