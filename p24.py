class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.methods = [self.printBalance,self.deposite,self.withdraw]

    def printBalance(self):
        print("Current Balance:",self.balance)

    def inputAmount(self):
        return float(input("Enter Amount:"))

    def deposite(self):
        amount = self.inputAmount()
        self.balance += amount
        self.printBalance()

    def withdraw(self):
        amount = self.inputAmount()
        if self.balance - amount <= 500:
            print("The Account Does Not Has Sufficient Balance.")
        else:
            self.balance -= amount
        self.printBalance()

var = Bank(10000)
while True:
    choice = int(input("select \n1. for checking balance.\n2. for deposite.\n3. for withdrawal.\n4. for exit."))
    if choice == 4: break
    else:
        var.methods[choice-1]()
