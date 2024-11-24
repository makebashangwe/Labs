email_list = []

def main_menu():
    print()
    print("[Mailing List]")
    print("1 - Add email")
    print("2 - Delete email")
    print("3 - List all emails")
    print("4 - Quit")
    print()
    while True:
        try:
            programChoice = int(input("Make your selection: "))
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
    if add_email not in email_list and add_email.strip():
        email_list.append(add_email)
        print("Email added to mailing list.")
        main_menu()
    elif not add_email.strip():
        print("Invalid Input. Please try again.")
        add_entry()
    else:
        print("Email already in list. Add anyway? Y/N")
        if input().upper() == "Y":
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
    for i, email in enumerate(email_list, start=1):
        print(email)
    main_menu()

def exit_program():
    print("Shutting down...")
    quit()

main_menu()
