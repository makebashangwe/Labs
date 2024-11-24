friends_list = {}

def main_menu():
    print()
    print("[Friend List]")
    print("1 - Add friend")
    print("2 - List friends")
    print("3 - Quit")
    print()
    while True:
        try:
            user = int(input("Make your selection: "))
            break
        except ValueError:
            print("Please enter a number selection.")
    
    match user:
        case 1:
            add_friend()
        case 2: 
            list_friends()
        case 3:
            exit_program()

def add_friend():
    name = input("Enter your friend\"s name: ")
    while not name.strip():
        print("Please enter a name.")
        name = input("Enter your friend\"s name: ")
    
    while True:
        try:
            age = int(input("Enter your friend\"s age: "))
            if age >= 0:
                break
            else:
                print("Please enter a positive integer for age.")
        except ValueError:
            print("Please enter a number.")
    
    if name not in friends_list:
        friends_list[name] = age
        print("Friend added")
    else:
        print("Friend already in list.")
    main_menu()      

def list_friends():
    if friends_list:
        for friend, age in friends_list.items():
            print(f"Name: {friend}, Age: {age}")
    else:
        print("No friends in the list.")
    main_menu()

def exit_program():
    print("Shutting down...")
    quit()

main_menu()
