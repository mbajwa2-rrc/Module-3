"""
Description: Understanding banking transactions in Python allows you to write a simple software that simulates basic banking functions including deposists, withdrawals, and balance queries.
Author: Mankirt Kaur Bajwa
Date: Oct 1, 2024
"""

import os
from time import sleep
import random

# Menu Options
MENU_OPTIONS = ["D", "W", "Q"]

# Initialize account balance 
account_balance = float(random.randint(-1000, 10000))



print("****************************************")
print("         PIXELL RIVER FINANCIAL")
print("             ATM Simulator")
print(f" Your current balance is: ${account_balance:,.2f}")
print("               Deposit: D")
print("              Withdraw: W")
print("                Quit: Q")
print("****************************************")

while True:
    selection = input("Enter your selection: ").upper()

    if selection not in MENU_OPTIONS:
        print("****************************************")
        print("           INVALID SELECTION")
        print("****************************************")
        

    if selection == MENU_OPTIONS[0] or selection == MENU_OPTIONS[1]:
        amount = float(input("Enter amount of transaction: "))
        if selection == MENU_OPTIONS[1]:
            if amount > account_balance:
                print("*" * 40)
                print("INSUFFICENT FUNDS". center(40))
                print("*" * 40)
            else:
                account_balance = account_balance - amount
        else:
            account_balance = account_balance + amount
        print("*" * 40)   
        print(f"  Your current balance is: ${account_balance:,.2f}")
        print("*" * 40)

    if selection == "Q":
            print("Thank you for using PIXELL RIVER FINICIAL ATM. Goodbye!")
    selection = input("Enter your selection").upper()

sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')    

