class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, initial_balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

account = BankAccount(account_number="123456789", customer_name="Ali", date_of_opening="2024-09-11", initial_balance=1000.0)
account.display_account_info()
account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.check_balance()}")
