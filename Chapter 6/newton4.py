#Python Programs Chapter 6 Project 4
#Restructure Newton’s method (Case Study: Approximating Square Roots) by decomposing it into three cooperating functions.
#The newton function can use either the recursive strategy of Project 1 or the iterative strategy of Case Study 3.6.
#The task of testing for the limit is assigned to a function named limitReached,
#whereas the task of computing a new approximation is assigned to a function named improveEstimate.
#Each function expects the relevant arguments and returns an appropriate value.


import math

def newton(x, estimate=1.0):
    tolerance = 0.000001
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, estimate)


def limitReached(diff, tolerance):
  if (diff <= tolerance):
        val = True
    else:
        val = False
    return val

def improveEstimate(x, square_root_function):
    return (square_root_function + x / square_root_function) / 2


def main():
    while True:
        x = input("Enter a positive number. Press enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        square_root_function = math.sqrt(x)
        improveEstimate(x, square_root_function)
        print("\nNewton's method estimate is ", newton(x))
        print("The Python function's estimate is ", square_root_function)


if __name__ == "__main__":
    main()
