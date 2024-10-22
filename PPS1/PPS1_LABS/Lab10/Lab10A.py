'''
Your program will feature a list which remembers every entry that is added to it. 
It will also contain a loop with the following options:
•	Add entry: prompts the user for an email address, and then adds it to the list.
•	Remove entry: prompts the user for an email address. If the email exists in the list, remove it. Otherwise, print out an error message.
•	List entries: List all emails in the mailing list.
•	Quit: Quits the program.

'''
#from termcolor import colored
import sys

email_list = []
#functions
def main_menu():
    print()
    print("[Mailing List]")
    print("1 - Add Email")
    print("2 - Delete Emal")
    print("3 - List all Emails")
    print("4 - Quit")
    print()
    while True:
        try:
            programChoice = int(input("Make your selecton: "))
            break
        except ValueError:
            print("Please enter a number selection.")
    match programChoice:
        case 1:
            add_entry()
        case 2:
            remove_entry()
        case 3:
            list_entries()
        case 4:
            exit_program()
def add_entry():
    add_email = input("Enter the email to be added: ")
    if add_email not in email_list and not (add_email == "" or add_email == " "):
        email_list.append(add_email)
        print("Email has been successfully added.")
        main_menu()
    elif add_email == " " or add_email == "":
        print("Invalid Input. Please try again.")
        add_entry()
    else:
        print("Email already in list. Add anyway?")
        add_anyway = input().upper()
        if add_anyway == "Y":
            email_list.append(add_email)
            print("Email added to mailing list.")
            main_menu()
        else:
            main_menu()

def remove_entry():
    remove_email = input("Enter the email to be removed: ")
    if remove_email in email_list:
        email_list.remove(remove_email)
        print(f"{remove_email} has been successfully removed.")
        main_menu()
    else:
        print(f"No such email in mailing list: {remove_email}")
        main_menu()

def list_entries():
    for i, email in enumerate(email_list, start = 1):
        print(i, '. ', email) 
         
    main_menu()    

def exit_program():
    print("Shutting down...")
    sys.exit()

main_menu()
