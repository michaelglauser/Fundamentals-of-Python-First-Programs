#Python Programs Chapter 6 Project 3
#Elena complains that the recursive newton function in Project 2 includes an extra argument for the estimate.
#The function’s users should not have to provide this value, which is always the same, when they call this function.
#Modify the definition of the function so that it uses a keyword argument with the appropriate default value, and call the function without a second argument to demonstrate that it solves this problem

import math

def newton(x, estimate = 1.0):
    tolerance = 0.000001
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    while True:
        x = input("Enter a positive number. Press enter/return to quit: ")
        if x == "":
             break
        x = float(x)

        print("\nNewton's method estimate is ", newton(x, 1))
        print("The Python function's estimate is ", math.sqrt(x))

if __name__ == "__main__":
    main()


