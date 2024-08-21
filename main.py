#توضیحات این  کد مه جیکار کردم کامنت می کنم
#یک کلاس ایجاد می کنیم
class BankSystem:
    def __init__(self):
        self.accounts = {}



#تابع برای درست کردن اکانت

    def create_account(self, username, password):
        if username in self.accounts:
            return "Account already exists."
        self.accounts[username] = {"password": password, "balance": 0}
        return "Account created successfully."

#تابع برای واریز پول

    def deposit(self, username, amount):
        if username not in self.accounts:
            return "Account not found."
        self.accounts[username]["balance"] += amount
        return f"Deposited {amount} successfully."

#تابع برای برداشت

    def withdraw(self, username, amount):
        if username not in self.accounts:
            return "Account not found."
        if self.accounts[username]["balance"] < amount:
            return "Insufficient balance."
        self.accounts[username]["balance"] -= amount
        return f"Withdrew {amount} successfully."

#تابع برای چک کردن حساب

    def check_balance(self, username):
        if username not in self.accounts:
            return "Account not found."
        return f"Your balance is {self.accounts[username]['balance']}."

#اجرا

    def run(self):
        while True:
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                print(self.create_account(username, password))
            elif choice == '2':
                username = input("Enter username: ")
                amount = int(input("Enter amount to deposit: "))
                print(self.deposit(username, amount))
            elif choice == '3':
                username = input("Enter username: ")
                amount = int(input("Enter amount to withdraw: "))
                print(self.withdraw(username, amount))
            elif choice == '4':
                username = input("Enter username: ")
                print(self.check_balance(username))
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = BankSystem()
    system.run()