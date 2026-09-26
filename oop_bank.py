class BankAccount:
    bank_name = "Python National Bank"

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


my_account = BankAccount()
my_account.balance = 0

print(my_account.bank_name)
print(my_account.balance)
print(my_account.get_balance())
my_account.deposit(100)
print(my_account.balance)
my_account.withdraw(30)
print(my_account.balance)

second_account = BankAccount()
second_account.balance = 500
second_account.deposit(50)
print(my_account.balance, second_account.balance)
print(second_account.bank_name)
