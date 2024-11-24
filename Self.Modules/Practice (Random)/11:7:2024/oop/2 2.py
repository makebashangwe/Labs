class BankAccount:
    def __init__(self,balance = 0):
        self.balance = balance

    def deposit (self):
        while True:
            try:
                desposit_amount = float(input("How much would you like to deposit?: "))
                break
            except ValueError:
                print("Please enter a number.")
        self.balance += desposit_amount
        print("Succcessfully deposited.")
        back_to_main = input("Would you like to return back to the main menu (Y/N)? ").upper()
        if "Y" in back_to_main:
            return
        elif "N" in back_to_main:
            quit()

        print(f"${desposit_amount} was successfully deposited.")
    def withdraw(self):
        if self.balance > 0:
            while True:
                try:
                    print(f"You currently have ${self.balance}.")
                    withdrawl_amount = float(input("How much would you like to withdraw?: "))
                    break
                except ValueError:
                    print("Enter a number please.")
            if withdrawl_amount <= self.balance:
                self.balance -= withdrawl_amount
                print ("Your funds were successfully withdrawn.")
            else:
                print("Not enough funds to withdraw that amount.")
        else:
            print("Not enough funds to withdraw.")
        back_to_main = input("Would you like to return back to the main menu (Y/N)? ").upper()
        if "Y" in back_to_main:
            return
        elif "N" in back_to_main:
            quit()
        else:
            return

    def checkbalance(self):
        print(f"You currently have ${self.balance}.")
        back_to_main = input("Would you like to return back to the main menu (Y/N)? ").upper()
        if "Y" in back_to_main:
            return
        elif "N" in back_to_main:
            quit()
                
def mainMenu(username,account):
        print(f"Hi, {username.title()}!")
        print("Please choose from the following options: ")
        print("1. Check Balance\n2.Deposit Funds\n3.Withdraw Funds\n4.Exit")
        while True:
            try:
                choice = int(input("Please enter a choice number: "))
                break
            except ValueError:
                print("Please enter a number between 1-4.")
        match choice:
            case 1:
                account.checkbalance()
            case 2:
                account.deposit()
            case 3:
                account.withdraw()
            case 4:
                quit()
    
username = input("Please enter your name: ")
account = BankAccount()
while True:
    mainMenu(username,account)

