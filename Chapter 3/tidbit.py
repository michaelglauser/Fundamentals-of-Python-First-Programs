#Python Programs Chapter 3 Project 10
#Write a program that takes the purchase price as input.
#The program should display a table, with appropriate headers, of a payment schedule for the lifetime of the loan.
#Each row of the table should contain the following items:
#        - the month number (beginning with 1)
#        - the current total balance owed
#        - the interest owed for that month
#        - the amount of principal owed for that month
#        - the payment for that month
#        - the balance remaining after payment
#The amount of interest for a month is equal to balance * rate / 12.
#The amount of principal for a month is equal to the monthly payment minus the interest owed.



purchase_price = float(input("Enter the puchase price: "))
down_payment = purchase_price * .10
month_number = 0
interest_rate = .12
starting_principal = purchase_price - down_payment
monthly_payment = starting_principal * .05
remaining_balance = starting_principal

print("%7s%18s%17s%18s%9s%16s" % \
      ("Month", "Starting balance",
       "Interest to pay", "Principal to pay",
       "Payment", "Remaining balance"))

while remaining_balance > 0:
    month_number += 1

    if remaining_balance > monthly_payment:
        remaining_balance_plus_interest = (remaining_balance * interest_rate) / 12
        remaining_principal_plus_interest = monthly_payment - remaining_balance_plus_interest
        principal_payment = remaining_principal_plus_interest + remaining_balance_plus_interest
        remaining_balance -= remaining_principal_plus_interest
    else:
        remaining_balance_plus_interest = 0
        remaining_principal_plus_interest = remaining_balance
        principal_payment = remaining_balance
        remaining_balance -= remaining_balance

    print("%7d%18.2f%17.2f%18.2f%9.2f%16.2f" % \
        (month_number, remaining_balance + remaining_principal_plus_interest, remaining_balance_plus_interest,
        remaining_principal_plus_interest, principal_payment, remaining_balance))