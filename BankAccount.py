class BankAccount:
  def __init__(self, full_name, account_number):
    self.name = full_name
    self.account = account_number
    self.balance = 0

  def deposit (self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount} New balance: ${self.balance}")
