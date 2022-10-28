# Import random module for random number selection
import random

# Created bank account class that takes full name as an argument
class BankAccount:
  def __init__(self, full_name):
    self.name = full_name
    # randomly generates 8 digit account number
    self.account_number = str(random.randint(10000000, 99999999))
    # starting balance set to 0
    self.balance = 0

  # DEPOSIT
  def deposit (self, amount):
    self.balance += amount
    print(f"Amount deposited: ${amount} New balance: ${self.balance}")

  # WITHDRAW
  def withdraw (self, amount):
    # If amount is less than balance, withdraw otherwise print insufficient funds
    if amount <= self.balance:
      self.balance -= amount
      print(f"Amount withdrawn: ${amount} New balance: ${self.balance}")
    else:
      print("Insufficient funds!")

  # GET BALANCE
  def get_balance (self):
    print(f"Your current account balance is: {self.balance}")
    return self.balance

  # ADD INTEREST based on monthly interest calculation
  def add_interest (self):
    self.balance += self.balance * 0.00083

  # PRINT BALANCE with name, account number, and balance
  def print_statement (self):
    # Sensitize account information to only show last 4 digits
    sensitized_account = "xxxx" + self.account_number[4] + \
        self.account_number[5] + \
        self.account_number[6] + self.account_number[7]
    print(f"{self.name}\nAccount No.: {sensitized_account}\nBalance: ${round(self.balance, 2)}")

# Stretch goal - create list called bank and loop over all accounts to add interest
bank = []
def bank_add_interest (bank):
  for account in bank:
    account.add_interest()

# Three bank account examples
account1 = BankAccount("Laurel McLean")
account2 = BankAccount("John Smith")
account3 = BankAccount("Dani Roxberry")

# Demonstrating methods
account1.print_statement()
account1.deposit(2200)
account1.add_interest()
account1.print_statement()

account2.print_statement()
account2.withdraw(300)

account3.print_statement()
account3.deposit(1000)
account3.withdraw(43)
account3.print_statement()

# Calling add interest stretch goal for all accounts
bank = [account1, account2, account3]
bank_add_interest(bank)
# printing statment again to demonstrate added interest
account3.print_statement()

# Example from assignment
# mitchell_account = BankAccount("Mitchell")
# mitchell_account.deposit(400000)
# mitchell_account.print_statement()
# mitchell_account.add_interest()
# mitchell_account.print_statement()
# # Bought Yeezy's
# mitchell_account.withdraw(150)
# mitchell_account.print_statement()


