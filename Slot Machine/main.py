import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line)
    return winnings, winning_lines

def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!!!")
        else:
            print("Please enter a positive number.")
        
    return amount

def get_number_of_lines():
   while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines.")
        else:
            print("Please enter a number.")
        
   return lines

def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[rows], end=" | ")
            else:
                print(column[rows], end="")
        
        print()

def get_bet():
    while True:
        bet = input("Enter the bet amount on each line(1-" + str(MAX_BET) +"): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Enter the valid bet amount.")
        else:
            print("Please enter a number.")
        
    return bet


def spin(balance):
    
    line = get_number_of_lines()

    while True:
        bet_amount = get_bet()
        total_bet = bet_amount * line
        if balance < total_bet:
            print(f"You do not have enough money, your current balance is ${balance}!")
        else:
            break

    print(f"Your are betting ${bet_amount} on {line}. Total bet is equal to: ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, line, bet_amount, symbol_value)
    print(f"You won ${winnings}.")
    print(f"Winning lines are:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    print("Thanks for playing!")

main() 
