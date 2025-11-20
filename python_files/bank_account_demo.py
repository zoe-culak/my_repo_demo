from bank_account import BankAccount #to use class for objects
account=BankAccount("123", 100) #account number, balance
print(account)
account.deposit(100)
account.withdraw(40)
print(account.get_balance())
account2=BankAccount("111")
print(account2)