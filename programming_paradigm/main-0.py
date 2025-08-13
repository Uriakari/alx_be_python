import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line interactions.
    """
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_args = sys.argv[1].split(':')
    command = command_args[0]
    
    try:
        if len(command_args) > 1:
            amount = float(command_args[1])
        else:
            amount = None # or handle a missing amount gracefully

        if command == "deposit" and amount is not None:
            account.deposit(amount)
        elif command == "withdraw" and amount is not None:
            account.withdraw(amount)
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            print("Usage: python main-0.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

    except ValueError:
        print("Error: Invalid amount. Please enter a number.")

if __name__ == "__main__":
    main()