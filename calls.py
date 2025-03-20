from accounts import *

def create_account():
    print("\nCreate a new account:")
    initial_amount = float(input("Enter the initial amount: "))
    account_name = input("Enter the account holder's name: ")
    account_type = input("Enter the account type (1 - Regular, 2 - Interest Rewards, 3 - Savings): ")

    if account_type == "1":
        return BankAccount(initial_amount, account_name)
    elif account_type == "2":
        return InterestRewardsAcct(initial_amount, account_name)
    elif account_type == "3":
        return SavingsAcct(initial_amount, account_name)
    else:
        print("Invalid account type. Creating a regular account by default.")
        return BankAccount(initial_amount, account_name)

def main():
    
    print("Welcome to the Bank Account Management System!")
    account1 = create_account()

    while True:
        print("\nWhat would you like to do?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account1.get_balance()
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
        elif choice == "4":
            amount = float(input("Enter the transfer amount: "))
            print("\nCreate the recipient account:")
            account2 = create_account()
            account1.transfer(amount, account2)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()