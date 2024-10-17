#Python Programs Chapter 6 Project 1
#Package Newton’s method for approximating square roots (Case Study: Approximating Square Roots) in a function named newton.
#This function expects the input number as an argument and returns the estimate of its square root.
#The script should also include a main function that allows the user to compute square roots of inputs until she presses the enter/return key.

import math

def newton(x):
	tolerance = 0.000001
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return estimate


def main():
    while True:
        x = input("Enter a positive number. Press enter/return to quit: ")
        if x == "":
            break
        x = float(x)

        print("The estimate is ", math.sqrt(x))


if __name__ == "__main__":
    main()