#Python Programs Chapter 6 Project 5
#A list is sorted in ascending order if it is empty or each item except the last one is less than or equal to its successor.
#Define a predicate isSorted that expects a list as an argument and returns True if the list is sorted, or returns False otherwise.


def isSorted(sorted_list):
    list_argument = sorted_list[:]
    list_argument.sort()
    if (list_argument == sorted_list):
        flag = 1
    else :
        flag = 0

    if (flag == 1):
        return (True)
    else:
        return (False)


def main():
    sorted_list = []
    print(isSorted(sorted_list))
    sorted_list = [1]
    print(isSorted(sorted_list))
    sorted_list = list(range(10))
    print(isSorted(sorted_list))
    sorted_list[9] = 2
    print(isSorted(sorted_list))

if __name__ == "__main__":
    main()