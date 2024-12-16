import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from datetime import date
import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('letsreadcreds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('lets_read')

logo= "" _          _   __                         _ 
 | |        | | /_/                        | |
 | |     ___| |_   ___   _ __ ___  __ _  __| |
 | |    / _ \ __| / __| | '__/ _ \/ _` |/ _` |
 | |___|  __/ |_  \__ \ | | |  __/ (_| | (_| |
 |______\___|\__| |___/ |_|  \___|\__,_|\__,_|

""


example = SHEET.worksheet('example')
data = example.get_all_values(0,1)
print(logo)
print(Style.BRIGHT+Fore.BLUE+'Welcome to Bible reading habit tracker!')
print(data)