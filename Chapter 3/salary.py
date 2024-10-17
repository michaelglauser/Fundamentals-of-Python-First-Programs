#Python Programs Chapter 3 Project 7
#Write a program that displays a salary schedule, in tabular format, for teachers in a school district. 
#The inputs are the starting salary, the percentage salary increase, and the number of years in the schedule. Each row in the schedule should contain the year number and the salary for that year.



starting_salary = input("Enter the teacher starting salary: $")

salary_increase = input("Enter the annual percentage increase: ")

percent_salary_increase = int(salary_increase) / 100

total_years = input("Enter the number of years: ")

count = 0

print("%4s%9s" % ("Year ", "Annual Salary"))

print("%12s" % ("------------------"))

for eachYear in range(0, int(total_years)):
    count += 1
    if count == 1:
        print("%4d%9.2f" % (count, float(starting_salary)))
    else:
        total_increase = float(starting_salary) * float(percent_salary_increase)
        starting_salary = float(starting_salary) + float(total_increase)
        print("%4d%9.2f" % (count, float(starting_salary)))