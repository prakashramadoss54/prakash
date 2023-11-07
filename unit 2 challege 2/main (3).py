
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.__account_balance}")

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Insufficient funds. Withdrawal unsuccessful.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder Name: {self.__account_holder_name}")
        print(f"Account Balance: ${self.__account_balance}")


# Example usage of the BankAccount class
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount(account_number="123456", account_holder_name="John Doe", initial_balance=1000)

    # Testing deposit and withdrawal functionality
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)
