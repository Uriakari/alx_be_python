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
        amount = None
        if len(command_args) > 1:
            amount = float(command_args[1])

        if command == "deposit":
            if amount is not None and amount > 0:
                account.deposit(amount)
            else:
                print("Error: Amount must be a positive number.")
        elif command == "withdraw":
            if amount is not None and amount > 0:
                account.withdraw(amount)
            else:
                print("Error: Amount must be a positive number.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            print("Usage: python main-0.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
            sys.exit(1)

    except (ValueError, IndexError):
        print("Error: Invalid amount. Please enter a number.")

if __name__ == "__main__":
    main()