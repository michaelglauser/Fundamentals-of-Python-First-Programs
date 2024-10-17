#Python Programs Chapter 6 Project 10
#Define and test a function myRange.
#This function should behave like Python’s standard range function, with the required and optional arguments, but it should return a list.
#Do not use the range function in your implementation!


def myRange(start = None, stop = None, step = None):
    argument_list = []
    for i in [start, stop, step]:
        if i is not None:
            argument_list.append(i)

    step = 1
    if len(argument_list) == 1:
        start = 0
        stop = argument_list[0]
    elif len(argument_list) == 2:
        start, stop = argument_list

        if start > stop: step = -1
    elif len(argument_list) == 3:
        start, stop, step = argument_list

    argument_function = []
    if step > 0:
        while start < stop:
            argument_function.append(start)
            start += step
    else:
        while start > stop:
            argument_function.append(start)
            start += step

    return argument_function


def main():
    print(" 2:", myRange(0, 10, 2))
    print(" 1:", myRange(0, 10))
    print(" 0:", myRange(10))
    print("-1:", myRange(10, 0))
    print("-2:", myRange(10, 0, -2))


if __name__ == "__main__":
    main()