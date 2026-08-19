class Bank:
    def __init__(self):
        self.balance=1000.0

    def deposit(self,amount):
        self.balance+=amount 

    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient funds")
        self.balance-=amount 

    def show_balance(self):
        print(f"Starting balance: ${self.balance:.2f}")

    #while True:
       # choice=input("Continue banking (d/w/s/x): ").lower()


    def main():
        bank=Bank()
        choice=input("Start banking :(d/w/s/x): ").lower()
        while choice!="x":
            if choice=="d":
                amount=float(input("Amount to deposit:$"))
                bank.deposit(amount)
                print(f"Amount deposited:${amount:.2f}")
            elif choice=="w":
                amount=float(input("Amount to withdraw:$"))
                try:
                    bank.withdraw(amount)
                    print(f"Amount withdrawn: ${amount:.2f}")
                except ValueError as error:
                    print(error)
            elif choice=="s":
                bank.show_balance()
            else:
                print("Invalid choice")
            choice=input("Continue banking (d/w/s/x): ").lower()



"""
        print("DeskBankApp started")
        deposit_amount=float(input("Amount to be desposited in $"))
        print(f"Amount ${deposit_amount:.2f} deposited")
        withdrawn_amount=float(input("Amount to be withdrawn in $"))
        print(f"Amount ${withdrawn_amount:.2f} withdrawn")
"""

if __name__=="__main__":
    Bank.main()