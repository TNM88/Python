class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in the account"):
        super().__init__(message)

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Withdrawal amount ({amount}) exceeds current balance ({self.balance}).")
        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: {self.balance}")

try:
    account = BankAccount(500)
    account.withdraw(600)
except InsufficientFundsError as e:
    print(e)
