import pandas as pd
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from datetime import date
from art import *
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

def get_entries(data, worksheet):
    #get entries from user
    while True:
        print("Please enter Your name.")
        input_name=input("Enter Your Name here:  \n)")
        worksheet=Sheet.worksheet({input_name})
        progress={inputname}.get_all_values
        print(progress)
        
example = SHEET.worksheet('example')
data = example.get_all_values()
print(welcome_msg[1])
print(welcome_msg[0])
print(Style.BRIGHT+Fore.BLUE+'Welcome to Let´s Read!/n Your Bible reading habit tracker!')
print(data)