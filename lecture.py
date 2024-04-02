# OOP Principles
# Encapsulation - Data Bundling
# Protecting class attributes when needed

# Public Attributes
# the model of a smart phone is something everyone can see
# self.model

# Protected Attributes _ <-- access modifier convention
# operating system - the phone and any 'children' of that phone would share
# can only be accessed through the object itself via methods
# self._operating_system

# Private Attributes __ <-- access modifier convention
# self.__serial_number
# sensitive information unique to that specific object
# that we only want accessible to the object itself

# using encapsulation with a smartphone
class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        # accessibility outside the class
        self.model = model # public attribute most accessible - least strict
        self._operating_system = operating_system #protected kind of accessible
        self.__serial_number = serial_number #private attribute not really accessible - most strict

    def show_info(self):
        # Accessing attributes within a class
        print(f"Model: {self.model}")
        print(f"Serial Number: Hidden for security purposes")
        print(f"Operating System: {self._operating_system}")

# creating an instance of our Smartphone class
my_phone = Smartphone("Iphone 13", "v5432698v754", "iOS")
# accessing our attributes via our method
my_phone.show_info()
# accesssing individual attribues
# public
print(my_phone.model)
# protected
# not a good practice to access protected variables directly
print(my_phone._operating_system)
# attribute error due to "name mangling"
# print(my_phone.__serial_number)


# Getters and Setters
# we use these to interact with protected and private variables within a class

class Smartphone:
    def __init__(self, model, serial_number, operating_system):
        # accessibility outside the class
        self.model = model # public attribute most accessible - least strict
        self._operating_system = operating_system #protected kind of accessible
        self.__serial_number = serial_number #private attribute not really accessible - most strict

    def show_info(self):
        # Accessing attributes within a class
        print(f"Model: {self.model}")
        print(f"Serial Number: Hidden for security purposes")
        print(f"Operating System: {self._operating_system}")
    # GETTER
    # getter for serial number
    def get_serial_number(self):
        return self.__serial_number
    
    # SETTER
    # setter for serial number
    def set_serial_number(self, new_number):
        self.__serial_number = new_number

# creating a object from the Smartphone class
my_phone = Smartphone("Iphone 13", "35v47cc354", "iOS")

# accessing the private attribute using a getter
print(f"My phone's Serial Number: {my_phone.get_serial_number()}") #safe way to access private data

# Modifying a private variable with a setter
my_phone.set_serial_number("vx5438mm045v68")
print(f"Updated Serial Number: {my_phone.get_serial_number()}")


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

# instantiating our account object
account = BankAccount("Ryan", 5)
# accessing account holder information - public attribute
print(f"Account Holder: {account.get_account_holder()}")
# access the balance information - private attribute
print(f"Initial Balance: ${account.get_balance()}")

# deposit some moneeeyyy
account.deposit(500)
# checking balance after depoist
print(f"Current Balance: ${account.get_balance()}")

# withdraw some money
account.withdraw(150)
print(f"Current Balance: ${account.get_balance()}")

# updating account holder
account.set_account_holder("Selena")
print(f"New Account Holder: {account.get_account_holder()}")

# setting routing number
account.set_routing_number(123456789)
print(account.get_routing_number())



# Inheritance
# parent class or superclass
class CellPhone():
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f"Making a call to {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# child class or subclass
# class that is inherited goes in the parentheses after the subclass is defined
class SmartPhone(CellPhone):
    # business as usual, we include any attributes we want to instantiate with
    def __init__(self, model, camera_resolution):
        # attributes that are inherited can be instantiated through the super().__init__
        # calls the init of the parent method, to assign the model attribute        
        super().__init__(model)
        # attribute unique to the child class
        self.camera_resolution = camera_resolution
    # methods dont need to be redefined in order to access them
    # method unique to the subclass
    def take_photo(self, photo):
        print(f"Taking a photo with {self.camera_resolution} resolution. Here it is {photo}")

# instantiate object from the parent class
cell_phone = CellPhone("Nokia 3390")
cell_phone.make_call('773202LUNA')
cell_phone.send_message("1234567890", "Hi sweetie, you forgot your lunch today. I left it with the front office.")
# cell_phone.take_photo(":)") <-- AttributeError

# instantiating object from the Child Class or Subclass
smart_phone = SmartPhone("Iphone 13", "4k")
# accessing attribute that was inherited from the parent class
print(smart_phone.model)
# accessing attribute unique to the child class
print(smart_phone.camera_resolution)
# calling methods inherited from the parent class
smart_phone.make_call("911")
smart_phone.send_message("6308528209", "Please leave me alone i dont want to talk about how we can be mutually beneficial to each other")
# calling method unique to the child class
smart_phone.take_photo("(ヘ･_･)ヘ┳━┳  (╯°□°）╯︵ ┻━┻")

# Method Overriding
# When a child class has a method of the same name as the parent class
# non class example
# def say_hello():
#     print("teletubbies, teletubbies, say HEL-LO HELLO")
# say_hello()

# def say_hello():
#     print("BOOOO BAHHHH LOOK WHAT I CAN DO")
# say_hello()

class CellPhone():
    def __init__(self, model):
        self.model = model

    def make_call(self, number):
        print(f"Making a call to {number}")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# cell_phone = CellPhone("Iphone 13")
# cell_phone.make_call("123456789")


# child class or subclass
# class that is inherited goes in the parentheses after the subclass is defined
class SmartPhone(CellPhone):
    # business as usual, we include any attributes we want to instantiate with
    def __init__(self, model, camera_resolution):
        # attributes that are inherited can be instantiated through the super().__init__
        # calls the init of the parent method, to assign the model attribute        
        super().__init__(model)
        # attribute unique to the child class
        self.camera_resolution = camera_resolution
    # methods dont need to be redefined in order to access them
    # method unique to the subclass
    def take_photo(self, photo):
        print(f"Taking a photo with {self.camera_resolution} resolution. Here it is {photo}")

    # overriding the make_call method from the parent class
    def make_call(self, number):
        # change the functionality of the parent class method to fit the needs of the child class
        print(f"Making a video call to {number} with {self.camera_resolution} resolution")

cell_phone = CellPhone("Iphone 13")
cell_phone.make_call("123456789")
smart_phone = SmartPhone("Iphone 13", "4k")
smart_phone.make_call("1234567890")




# importing our SavingsAccount and CheckingAccount from accounts.py
from accounts import SavingsAccount, CheckingAccount
savings = SavingsAccount("Ryan", 2000, .05)
checking = CheckingAccount("Ryan", 1000, 5)

# savings account usage
savings.add_interest() # adds interest based on our current balance and the interest rate
savings.withdraw(501) # calling overridden withdraw method - withdrawal limit exceeded
savings.withdraw(100) # defaults back to the original parent method- super().withdraw()
print(savings.get_balance())

# checking account
checking.deposit(500) # call the parent method by default, because we didnt override
checking.withdraw(300) # hits ya with the transaction fee
print(f"Checking Account Balance: {checking.get_balance()}")

# Polymorphism - the ability of objects of different classes to respond to the same method call in
# their own unique ways. also turns people into sheep
class SmartPhone():
    def __init__(self, model):
        self.model = model

    def download_app(self, app_name):
        print(f"Downloading {app_name} in a generic way")

class AndroidPhone(SmartPhone):
    def __init__(self, model):
        super().__init__(model)
    
    def download_app(self, app_name):
        print(f"Downloading {app_name} from Google Play Store")


class IPhone(SmartPhone):
    def __init__(self, model):
        super().__init__(model)
    
    def download_app(self, app_name):
        print(f"Downloading {app_name} from Apple Store")

galaxy = AndroidPhone("Galaxy27")
galaxy.download_app("Candy Crush")

iphone = IPhone("Iphone13")
iphone.download_app("Candy Crush")






    

    






