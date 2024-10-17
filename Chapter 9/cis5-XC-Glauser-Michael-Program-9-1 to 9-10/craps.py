#Python Programs Chapter 9 Project 6
#Revise the Player class in the craps game, so that its user can make individual rolls of the dice and view the results after each roll.

from die import Die

class Player(object):

    def __init__(self):

        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []

    def __str__(self):

        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):

        return len(self.rolls)

    def play(self):
       

        self.rolls = []
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        initialSum = v1 + v2
        if initialSum in (2, 3, 12):
            return False
        elif initialSum in (7, 11):
            return True
        while (True):
            self.die1.roll()
            self.die2.roll()
            (v1, v2) = (self.die1.getValue(),
                        self.die2.getValue())
            self.rolls.append((v1, v2))
            laterSum = v1 + v2
            if laterSum == 7:
                return False
            elif laterSum == initialSum:
                return True

def playOneGame():

    player = Player()
    youWin = player.play()
    print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):

    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in range(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of player wins is", wins)
    print("The total number of player losses is", losses)
    print("The average number of rolls per each player win is %0.2f" % \
          (winRolls / wins))
    print("The average number of rolls per each player loss is %0.2f" % \
          (lossRolls / losses))
    print("The player winning percentage is %0.3f" % (wins*100 / number)+"%")

def main():

    number = int(input("Enter the total number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()