''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab 4C
'''

logged_in = True
balance = 1000
print("Welcome!")
print(f"You have ${balance} in your account.")

while logged_in == True:

    print("""Menu
         0 – Make a deposit
         1 – Make a withdrawal
         2 – Display account value
    """)
    selection = int(input("Please make a selection: "))

    match selection:
        case 0:
            deposit = float(input("How much would you like to deposit?: "))
            balance = balance + deposit
            print(f"Your current balance is ${balance:.1f}")
            mainmenu = input("Would you like to return to the main menu (Y/N)?: ")
            mainmenu = mainmenu.upper()
            if mainmenu == "Y":
                logged_in = True
            elif mainmenu == "N":
                logged_in = False
            else:
                print("Invalid Input. Please try again.")

        case 1:
            withdrawal = float(input("How much would you like to withdraw?: "))
            if balance < withdrawal:
                print("Not enough balance. Withdrawal cancelled.\n"
                      f"Your current balance is {balance:.1f}")

            else:
                balance = balance - withdrawal
                print(f"Your current balance is ${balance:.1f}")

            mainmenu = input("Would you like to return to the main menu (Y/N)?: ")
            mainmenu = mainmenu.upper()
            if mainmenu == "Y":
                logged_in = True
            elif mainmenu == "N":
                logged_in = False
            else:
                print("Invalid Input. Please try again.")

        case 2:
            print(f"Your current balance is ${balance}")
            mainmenu = input("Would you like to return to the main menu (Y/N)?: ")
            mainmenu = mainmenu.upper()
            if mainmenu == "Y":
                logged_in = True
            elif mainmenu == "N":
                logged_in = False
            else:
                print("Invalid Input. Please try again.")

        case _:
            print("Invalid Entry, please try again.")
            mainmenu = input("Would you like to return to the main menu (Y/N)?: ")
            mainmenu = mainmenu.upper()
            if mainmenu == "Y":
                logged_in = True
            elif mainmenu == "N":
                logged_in = False
            else:
                print("Invalid Input. Please try again.")


if logged_in == False:
    print("Thank you for banking with us!")