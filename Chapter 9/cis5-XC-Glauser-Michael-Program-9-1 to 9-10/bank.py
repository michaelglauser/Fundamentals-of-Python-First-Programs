#Python Programs Chapter 9 Project 3
#The str method of the Bank class returns a string containing the accounts in random order. 
#Design and implement a change that causes the accounts to be placed in the string by order of name.

import pickle
import random
from savingsaccount import SavingsAccount


class Bank:
    
    def __init__(self, fileName=None):
        

        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):

        return "\n".join([str(v) for (k, v) in
                          sorted(self.accounts.items(),
                                 key=lambda cv: cv[1].userName())])

    def makeKey(self, name, pin):

        return name + "/" + pin

    def add(self, account):

        key = self.makeKey(account.userName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):

        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):

        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def interestRate(self):

        total = 0
        for account in self.accounts.values():
            total += account.interestRate()
        return total

    def getKeys(self):

        return []

    def save(self, fileName=None):

        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

def createBank(numAccounts=1):
    names = ("BamBam", "Sven", "Bernardinho", "Stavros", "Fred",
             "Wilma", "Pebbles", "Gunther")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank


def testAccount():

    account = SavingsAccount("Wilma", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.userBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.userBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.userBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.userBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.userBalance())


def main(number=10, fileName=None):

    testAccount()

    print("\n----------Account details------------\n")
    if fileName:
        bank = Bank(fileName)
    else:
        bank = createBank(number)
        print(bank)


if __name__ == "__main__":
    main()