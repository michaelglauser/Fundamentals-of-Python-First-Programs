#Python Programs Chapter 3 Project 3
#Modify the guessing-game program on pages 90-91, so that the user thinks of a number that the computer must guess.


import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
maximum_number_of_guesses = round(math.log(larger - smaller + 1, 2))
while True:
    count += 1
    print(smaller, larger)
    yourNumber = (smaller + larger) // 2
    print("Your number is", yourNumber)
    answer = input("Enter =, <, or >: ")
    if answer == "=":
        print("Congratulations, I guessed it in", count, "tries!")
        break
    elif count == maximum_number_of_guesses:
        print("I have run out of guesses.")
        break
    elif answer == "<":
        larger = yourNumber - 1
    else:
        smaller = yourNumber + 1