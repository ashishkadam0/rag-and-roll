class BankAccount:
    """A simple class that keeps each account's data separate."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_summary(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


ashish_account = BankAccount("Ashish", 1000)
komal_account = BankAccount("Komal", 500)

ashish_account.deposit(250)
ashish_account.withdraw(400)
ashish_account.display_summary()

komal_account.withdraw(100)
komal_account.display_summary()

# Exercise:
# Add a transfer(self, target_account, amount) method that withdraws money
# from the current account and deposits it into another BankAccount object.