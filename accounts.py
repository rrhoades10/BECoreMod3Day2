#    location     thing we're importing
from bank import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    # method to add interest to the balance
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} added to balance")
        print(f"Your new balance is {self.get_balance()}")

    # Override the withdraw method
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded")
        else:
            # calls the original withdraw method
            super().withdraw(amount)

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, transaction_fee):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    # override the the withdraw method to include a transaction fee
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.get_balance():
            self.set_balance(self.get_balance() - total_amount)
            print(f"Withdrawn: {amount}, Transaction fee: {self.transaction_fee}")
