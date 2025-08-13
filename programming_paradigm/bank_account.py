class BankAccount:
    """
    A class to represent a bank account.

    Attributes:
        __account_balance (float): The balance of the bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a BankAccount instance.

        Args:
            initial_balance (float): The starting balance for the account.
        """
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount. Amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount must be positive.")
        else:
            print("Insufficient funds.")
        return False

    def display_balance(self):
        """
        Prints the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

if __name__ == "__main__":
    # Example usage of the BankAccount class
    account = BankAccount(100)
    account.display_balance()
    account.deposit(50)
    account.display_balance()
    account.withdraw(20)
    account.display_balance()
    account.withdraw(200)
    account.display_balance()