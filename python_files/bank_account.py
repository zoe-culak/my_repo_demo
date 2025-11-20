# Declare the class BankAccount
# Python convention is to capitalize first letter in each word of class name
class BankAccount:
    # __init__ method is like the constructor in Java
    # instance variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java-- but NOT optional (required)
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    # __str__ is like the toString() method in Java
    # it is called when the object is printed
    # it's used for debugging purposes
    def __str__(self):
        return f"{self.account_number}  has the balance  {self.balance}"

    # first parameter in class methods MUST be self, ignore the self parameter, when you call deposit just add parameter of amount
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance
