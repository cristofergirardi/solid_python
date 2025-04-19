class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute (single underscore)
        self.__balance = balance  # Private attribute (double underscore - name mangling)

    # Getter method for the private attribute
    def get_balance(self):
        return self.__balance

    # Setter method for the private attribute
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance")

    # Public method that uses the private attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    # Public method that uses the private attribute
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

# Testing the encapsulation
account = BankAccount("123456", 1000)

# Accessing the protected attribute (not recommended, but possible)
print("Account number:", account._account_number)

# Accessing and modifying the private attribute through getter and setter methods
print("Initial balance:", account.get_balance())
account.set_balance(500)
print("Updated balance:", account.get_balance())

# Using public methods that internally use the private attribute
account.deposit(100)
print("Balance after deposit:", account.get_balance())
account.withdraw(50)
print("Balance after withdrawal:", account.get_balance())
