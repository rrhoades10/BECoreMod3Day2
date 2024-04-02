class BankAccount():
    def __init__(self, account_holder, initial_balance = 0):
        self.__balance = initial_balance #private attribute
        self.account_holder = account_holder # public attribute
        self.routing_number = 0
       
    # setter for routing_number
    def set_routing_number(self, number):
        if isinstance(number, int):
            self.routing_number = number
        else:
            print("please enter a valid routing number")
    # getter for routing number
    def get_routing_number(self):
        return self.routing_number
    # getter for balance
    def get_balance(self):
        return self.__balance
    
    # setter for balance
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # getter for account_holder
    def get_account_holder(self):
        return self.account_holder
    
    # setter for account_holder
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder

    def deposit(self, amount):
        if amount > 0:
            # sets balance to   current balance + amount to be deposited
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: ${amount}! Great job!")
        else:
            print("Invalid deposit amount...")

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            # sets balance to   current balance - amount to be withdrawn
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal amount or insufficient funds")