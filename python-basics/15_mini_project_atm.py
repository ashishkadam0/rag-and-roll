#Mini Project

balance = 1000
correct_pin = 1234


# Function to check balance
def check_balance():
    print(f"\nYour current balance is: ₹{balance}")


# Function to deposit money
def deposit():
    global balance

    try:
        amount = int(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance += amount
            print(f"₹{amount} deposited successfully!")
            print(f"New balance: ₹{balance}")
        else:
            print("Amount must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a number.")


# Function to withdraw money
def withdraw():
    global balance

    try:
        amount = int(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient balance!")

        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully!")
            print(f"Remaining balance: ₹{balance}")

    except ValueError:
        print("Invalid input! Please enter a number.")


# Ask for PIN
try:
    pin = int(input("Enter your 4-digit PIN: "))

    if pin == correct_pin:

        print("\nLogin successful!")

        # Keep showing menu until user chooses Exit
        while True:

            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("======================")

            choice = input("Choose an option: ")

            if choice == "1":
                check_balance()

            elif choice == "2":
                deposit()

            elif choice == "3":
                withdraw()

            elif choice == "4":
                print("\nThank you for using the ATM!")
                break

            else:
                print("Invalid option! Please choose 1, 2, 3, or 4.")

    else:
        print("Incorrect PIN!")

except ValueError:
    print("Invalid PIN! Please enter numbers only.")