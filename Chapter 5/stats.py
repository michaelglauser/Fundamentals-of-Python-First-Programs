#Python Programs Chapter 5 Project 1
#A group of statisticians at a local college has asked you to create a set of functions that compute the median and mode of a set of numbers, as defined in Section 5.4.
#Define these functions in a module named stats.py. Also include a function named mean, which computes the average of a set of numbers.
#Each function should expect a list of numbers as an argument and return a single number. Each function should return 0 if the list is empty.
#Include a main function that tests the three statistical functions with a given list.

def median(numbers):
    numbers.sort()
    number_listing = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[number_listing]
    else:
        return (numbers[number_listing] + numbers[number_listing - 1]) / 2

def mean(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def mode(numbers):
    result = numbers[0]
    count = 0

    for number_calculator in numbers:
        if numbers.count(number_calculator) >= count:
            count = numbers.count(number_calculator)
            result = number_calculator

    return result

def main():

    given_list = [3, 1, 7, 1, 4, 10]

    print("List:", given_list)
    print("Mode:", mode(given_list))
    print("Median:", median(given_list))
    print("Mean:", mean(given_list))


main()