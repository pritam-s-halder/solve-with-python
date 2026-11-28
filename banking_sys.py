class Information:
    def __init__(self, name, acc_no):
        self.name = name
        self.acc_no = acc_no


class Account(Information):
    def __init__(self, name, acc_no, balance=0):
        super().__init__(name, acc_no)
        self.balance = balance

    def get_balance(self):
        return self.balance

    def credit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.balance += amount
        print(f"Amount credited = {amount}")
        print(f"Total balance = {self.get_balance()}")

    def debit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Amount debited = {amount}")
            print(f"Total balance = {self.get_balance()}")


class FixedDeposit(Information):
    def __init__(self, name, acc_no, amount, annual_rate, compounds_per_year, years):
        super().__init__(name, acc_no)
        self.amount = amount
        self.annual_rate = annual_rate
        self.compounds_per_year = compounds_per_year
        self.years = years

    def calculate_interest(self):
        rate = self.annual_rate / 100
        n = self.compounds_per_year
        final_amount = self.amount * (1 + rate / n) ** (n * self.years)
        interest_earned = final_amount - self.amount
        print(f"Interest earned = {interest_earned:.2f}")
        print(f"Maturity amount = {final_amount:.2f}")


class Loan(Information):
    def __init__(self, name, acc_no, amount, annual_rate, compounds_per_year, years):
        super().__init__(name, acc_no)
        self.amount = amount
        self.annual_rate = annual_rate
        self.compounds_per_year = compounds_per_year
        self.years = years

    def calculate_interest(self):
        rate = self.annual_rate / 100
        n = self.compounds_per_year
        total_repayable = self.amount * (1 + rate / n) ** (n * self.years)
        interest_payable = total_repayable - self.amount
        print(f"Interest payable = {interest_payable:.2f}")
        print(f"Total repayable = {total_repayable:.2f}")


acc = Account("Aarav", 101, 1000)
acc.credit(500)
acc.debit(300)
acc.debit(5000)

fd = FixedDeposit("Aarav", 102, 10000, 6, 4, 2)
fd.calculate_interest()