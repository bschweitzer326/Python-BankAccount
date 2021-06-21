class BankAccount:
    def __init__(self, account, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.account = account

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("Insufficient Funds: Charging a $5 fee!")
        return self

    def display_account_info(self):
        print(f"{self.account} interest rate is {self.int_rate} and account balance is ${round(self.balance,2)}.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        elif self.balance <= 0:
            self.balance = self.balance
        return self

checking = BankAccount("checking", .02, 0)
savings = BankAccount("savings", .02, 0)

checking.deposit(100).deposit(500).deposit(300.05).withdraw(200).yield_interest().display_account_info()
savings.deposit(200).deposit(100).withdraw(50).withdraw(50).withdraw(150).withdraw(100).yield_interest().display_account_info()

