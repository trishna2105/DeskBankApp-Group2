class Bank:
    @staticmethod
    def main():
        print("DeskBankApp started")
        deposit_amount=float(input("Amount to be desposited in $"))
        print(f"Amount ${deposit_amount:.2f} deposited")
        withdrawn_amount=float(input("Amount to be withdrawn in $"))
        print(f"Amount ${withdrawn_amount:.2f} withdrawn")

if __name__=="__main__":
    Bank.main()