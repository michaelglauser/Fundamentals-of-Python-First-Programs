#Python Programs Chapter 2 Project 10
#Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours, and displays an employee's total weekly pay.


hourly_wage = float(input("Provide the hourly wage: $"))
regular_hours = int(input("Provide the total regular hours: "))
overtime_hours = int(input("Provide the total overtime hours: "))

weekly_pay_regular_hours = float(hourly_wage) * int(regular_hours)
weekly_pay_overtime_hours = int((1.5 * hourly_wage) * overtime_hours)

print("The employee's total weekly pay is: $" + str(weekly_pay_regular_hours + weekly_pay_overtime_hours))