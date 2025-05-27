class Account:
    interest_rate = 0.05
    minimum_balance = 200
    def __init__(self,name,account_number):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.account_number = account_number
        self.transactions = []
        self.loan_approved = False
        self.is_frozen = False

      


    def deposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"Confirmed you have sucessfully deposited KSH.{amount}. Your new account balance is KSH{self.balance}")

     
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
                print(f"Your withdrawal was unsuccessful. You cannot withdraw an amount less than KSH.{self.min_balance}")
        if amount <= self.balance:
            self.balance -= amount          
            print(f"You have successfully withdrawn KSH.{amount}. Your new balance is KSH.{self.balance}")  
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        
        else:
            print("Insufficient funds")
        
    def get_balance(self):
        return self.balance


    def transfer_funds(self,recipient, amount):
        if amount>0  and amount <= self.balance:
            self.withdraw(amount)
            recipient.deposit(amount)
            print(f"You have transferred KSH.{amount} to {recipient.account_number}")
        else:
            print("You have insufficient funds") 


    def request_loan(self, amount):
        if amount<=0:
            return "Loan amount must be positive."
        if self.balance >= 100:
            self.loan_approved = True
            self.balance += amount
            return f"Congratulations. Your loan of KSH.{amount} has been approved"
        else:
            return "Your loan request has been denied."


    def repay_loan(self,amount):
        self.loan_approved -= amount
        self.balance -= amount
        return f"You have repaid KSH.{amount} successfully"


    def view_account_details(self):
        return f"Hello {self.name}, your account number is {self.account_number} and you have a balance of {self.balance}"

    def change_account_owner(self, new_owner):
        self.name=new_owner
        return f"owner of this account is {self.name}"

    def account_statement(self):
        print(f"Account statement for {self.name}")
        print("-" * 40)
        if not self.transactions:
            print("No transactions available")
        else:
            index = 1
            for transaction in self.transactions:
                print(f"{index}. {transaction}")
                index += 1
        print("-" * 40)
          


    def interest_calculation(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Your newbalance is KSH.{self.balance}")

    def freeze_account(self):
        self.is_frozen = True
        print("Your account has been frozen")

    def unfreeze_account(self):
        self.is_frozen = False
        print("Your account is now active")

    def min_balance(self,amount):
        return (self.balance - amount) >= self.minimum_balance


    def close_account(self):
        self.balance = 0.0
        self.transactions.clear()
        self.is_frozen = True
        print("This account has been closed. You do not have any balance.")
        
        


