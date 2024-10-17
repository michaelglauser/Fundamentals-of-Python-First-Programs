#Python Programs Chapter 6 Project 2
#Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton. 


import math

def newton(x, estimate):
    tolerance = 0.000001
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, estimate)


def main():
    while True:
        x = input("Enter a positive number. Press enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        estimate = 1.0
        print("\nNewton's method estimate is ", newton(x, estimate))
        print("The Python function's estimate is ", math.sqrt(x))


if __name__ == "__main__":
    main()







