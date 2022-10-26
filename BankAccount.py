class BankAccount:
  def __init__(self, full_name, account_number):
    self.name = full_name
    self.account = account_number
    self.balance = 0

  def deposit (self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount} New balance: ${self.balance}")

  def withdraw (self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Amount withdrawn: ${amount} New balance: ${self.balance}")
    else:
      print("Insufficient funds!")

  def get_balance (self):
    print(f"Your current account balance is: ${self.balance}")
    return self.balance

  