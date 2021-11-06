class BankAccount:
    # Magic methods
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def display(self):
        print(self.account_number, self.account_name, self.balance, "₫")

    def withdraw(self, amount):
        self.balance -= amount

    def deposite(self, amount):
        self.balance += amount
        print("Balance:", self.balance)


my_account = BankAccount(1, "Ba")

my_account.display()
my_account.deposite(1_000_000_000_000_000)  # 😊
