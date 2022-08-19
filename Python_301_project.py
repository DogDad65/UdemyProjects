
class Banking:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def transaction_log(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def withdraw(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.transaction_log(f"Withdraw {amount}")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction_log(f"Deposit {amount}")


account = Banking(100.50)
while True:
    try:
        action = input("Good Day! What would you like to do? ")
    except KeyboardInterrupt:
        print("\nThank You! Have a great day!\n")
        break
       
    if action in ["withdraw", "deposit"]:
        if action == "withdraw":
            amount = input("What would you like to withdraw? ")
            account.withdraw(amount)
        else:
            amount = input("How much would you like to deposit? ")
            account.deposit(amount)

        print("Your current balance is ", account.balance)
    else:
        print("That is not a valid action. Please try again. ")


    
  








  





