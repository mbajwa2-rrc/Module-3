"""
Description: This application detrmines and applies interest to customer accounts based on their balances. 
Author: Mankirt Kaur Bajwa
Date: Oct 3rd, 2024
"""

import csv
from pprint import pprint


accounts = {}


with open('account_balances.txt', 'r') as file:
    for line in file:
        account, balance = line.strip().split('|')
        accounts[account] = float(balance)


print("Current Balances:")
pprint(accounts)


for account, balance in accounts.items():
    if balance < 0:
        # Negatiive balances incur a 10% interest charge
        rate = 0.10
    elif balance < 1000:
        # Positive balance less than $1000.00 earn 1.0% interest
        rate = 0.01
    elif balance < 5000:
        # Positive balance $1000.00 or greater but less than $5000.00 earn 2.5% interest
        rate = 0.025
    else: 
        # Positive balances $5000.00 or greater earn 5.0% interest
        rate = 0.05


new_balance = balance + ((balance * rate) / 12)
accounts[account] = new_balance


print("/nUpdated Balances after Interest Calculation:")
pprint(accounts)



initials = 'MB'  
csv_filename = f'updated_balances_MB.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Account', 'Balance'])  
    for account, balance in account_balances.items():
        writer.writerow([account, f"{balance:.6f}"])  
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

filename = 'updated_balances_MB.csv' 
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Account', 'Balance'])
    for account, balance in accounts.items():
        writer.writerow([account, f"{balance:6f}"])

print(f"/nUpdated balances written to {filename}.")


with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print("\nContents of the Updated Balances CSV:")
    for row in reader:
        print(row)

