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
        self.balance += balance
        print(f"Successfully done! €{balance:.2f} Balance: €{self.balance:.2f}")
