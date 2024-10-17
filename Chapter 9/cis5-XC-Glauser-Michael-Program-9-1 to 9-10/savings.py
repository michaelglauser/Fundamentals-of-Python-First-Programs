#Python Programs Chapter 9 Project 3
#The str method of the Bank class returns a string containing the accounts in random order. 
#Design and implement a change that causes the accounts to be placed in the string by order of name.


class SavingsAccount:

    RATE = 0.02  

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):

        result = 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def userBalance(self):

        return self.balance

    def userName(self):

        return self.name

    def getPin(self):

        return self.pin

    def deposit(self, amount):
        
        self.balance += amount
        return None

    def withdraw(self, amount):
       

        if amount < 0:
            return "Amount must be greater than or equal to 0"
        elif self.balance < amount:
            return "Not enough funds in your bank account"
        else:
            self.balance -= amount
            return None

    def interestRate(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest