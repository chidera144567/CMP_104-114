class Account:
    def __init__(self):
        self.name = "Chidera"
        self.account_number = 49494033030
        self.account_balance = 200000

    def deposite(self, amount):
        self.account_balance = self.account_balance + amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        print(self.account_balance)