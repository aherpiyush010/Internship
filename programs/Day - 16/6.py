# Create a BankAccount Class
# Attributes:
# account_holder, balance.
# Methods:
# deposit(amount) — Adds money.# withdraw(amount) — Subtracts money if available.
# display_balance() — Shows the balance.
# Test it: Create an account, deposit money, withdraw money, and display the balance

class BankAccount:
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder 
        self.balance = balance
    
    def deposit(self , amount):
        self.balance = self.balance + amount
        print("Ammount deposited sucessfull ..")
        print(f"{self.account_holder} your balance after deposite : {self.balance}")
        
    def withdraw(self , amount):
        
        if(self.balance == 0):
            print("""your account balance is 0 ..
                   first add amount in account ..""")
        elif(self.balance < amount):
            print("your ammount is more than your account balance ..")
        else:
            print("Ammount withdraw sucessfull ..")
            self.balance = self.balance - amount
            
        print(f"{self.account_holder} your balance after withdraw : {self.balance}")
        
    def create_acc(self):
        print(f" The name of account holder : {self.account_holder}")
        print(f" your bank balance is : {self.balance}")
obj = BankAccount("piyush ",0)
obj.deposit(1000000)
obj.withdraw(2000)
obj.withdraw(1500000)
        