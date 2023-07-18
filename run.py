import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cashpoint')


class atm_machine:
    def __init__(self, account_number, pin):
        self.account_number = account_number
        self.pin = pin
        self.balance = 1500

    def deposit(self, balance):
        self.deposit += balance
        print(f"Done! €{balance:.2f} Balance: €{self.balance:.2f}")

    def withdraw(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            print(f"Done! €{balance:.2f} Balance: €{self.balance:.2f}")
        else:
            print("Insufficient balance.")

    def transfer(self, balance, destination_account):
        if self.balance >= balance:
            self.balance -= balance
            destination_account.balance += balance
            print(f"Successfully done! €{balance:.2f}")
            print(f"current balance: €{self.balance:.2f}")
        else:
            print("Insufficient balance for transfer.")

    def options(self):
        print("Options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check balance")
        print("0. Exit")


account_number = input("Enter your account number:\n ")
pin = input("Enter your PIN: ")
atm = atm_machine(account_number, pin)

while True:
    atm.options()
    options = input("Enter the desired option number:\n ")

    if options == "0":
        break

    if options == "1":
        balance = float(input("Enter the deposit amount:\n €"))
        atm.deposit(balance)

    elif options == "2":
        balance = float(input("Enter the withdraw amount:\n €"))
        atm.withdraw(balance)

    elif options == "3":
        balance = float(input("Enter the transfer amount:\n €"))
        destination_account = atm_machine(account_number, pin)
        atm.transfer(balance, destination_account)

    elif options == "4":
        atm.check_balance()

    else:
        print("Invalid option. Please try again.")

print("Thanks for using Cash point.")
