import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROW = 3
COLS = 3

system_count = {
    'A': 2,
    'B': 3,
    'c': 4
}

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit() or amount.startswith('-'):
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount
def get_number_of_lines():
    while True:
        line  = input('Enter the number of lines to bet on (1 -' + str(MAX_LINE) + ')? ')
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print('Please enter a valid number of lines.')
        else:
            print('Please enter a number.')
    return line

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit() or amount.startswith('-'):
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}.')
        else:
            print('Please enter a number.')
    return amount

def main():
     balance = deposit()
     line = get_number_of_lines()
     while True:
         bet = get_bet()
         total_bet = bet * line
         if total_bet > balance:
             print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
         else:
             break
     print(f'You are betting ${bet} on {line}. Total bet is equal to: ${total_bet}')

main()