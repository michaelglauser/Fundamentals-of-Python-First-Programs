#Python Programs Chapter 9 Project 6
#Revise the Player class in the craps game, so that its user can make individual rolls of the dice and view the results after each roll.
#Define the Die class.

from random import randint

class Die:


    def __init__(self):

        self.value = 1

    def roll(self):

        self.value = randint(1, 6)

    def getValue(self):

        return self.value

    def __str__(self):

        return str(self.getValue())