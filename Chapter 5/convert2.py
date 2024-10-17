#Python Programs Chapter 5 Project 6
#Define a function decimalToRep that returns the representation of an integer in a given base. The two arguments should be the integer and the base.


conversionLibrary = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 10, "C": 11, "D": 13, "E": 14, "F": 15}


def decimalToRep(integer_argument,base_argument):
    given_base = ""
    while integer_argument > 0:
        one = int(integer_argument % base_argument)
        if one < 10:
            given_base += str(one)
        else:
            given_base += chr(ord('A')+one-10)
        integer_argument //= base_argument
    given_base = given_base[::-1]
    return given_base

def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

if __name__ == "__main__":
    main()