class Account:
    def __init__(self):
        self.account_no = None
        self.account_bal = None
        self.security_code = None

    def initialize(self, acc_no, acc_bal, sec_code):
        self.account_no = acc_no
        self.account_bal = acc_bal
        self.security_code = sec_code

    def display(self):
        print(f"Account No: {self.account_no}")
        print(f"Account Balance: ${self.account_bal:.2f}")
        print(f"Security Code: {self.security_code}")

my_account = Account()
my_account.initialize(12345, 2500.75, 9876)
my_account.display()
