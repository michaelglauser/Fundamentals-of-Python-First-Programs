#Python Programs Chapter 5 Project 5
#Define a function named repToDecimal that expects two arguments, a string, and an integer.
#The second argument should be the base.


conversionLibrary = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 10, "C": 11, "D": 13, "E": 14, "F": 15}

def repToDecimal(n, fromBase):
    integer_argument = 0
    power = 0

    for i in range((len(n)), 0, -1):
        integer_argument += conversionLibrary[n[i-1]] * (int(fromBase) ** power)
        power += 1
    return(integer_argument)

def main():
    print(repToDecimal('10', 10))
    print(repToDecimal('10', 8))
    print(repToDecimal('10', 2))
    print(repToDecimal('10', 16))

if __name__ == "__main__":
    main()