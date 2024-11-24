
friends_list = {}

def main_menu():
    print("[Friends List]")

    print("1 - Add Friend")
    print("2 - List Friends")
    print("3 - Quit")

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
    
    while True:
        while True:
            name = input("Enter your friend's name: ")
            if name == "" or name == " ":
                print("Please enter a name.")
            else:
                break
        try:
            age = int(input("Enter your friend's age:"))
            if age < 0:
                print("Please enter a positive integer for age.")
            else:
                break
        except ValueError:
            print("Please enter a number.")

    if name not in friends_list:
        friends_list[name] = age
        print("Added successfully.")
    else:
        print("Friend already in list.")
    main_menu()      
    
def list_friends():
    if friends_list:
        for friend,age in friends_list.items():
            print(f"Name: {friend.capitalize()}, Age: {age}")
    else:
        print("No friends in the list.")

    main_menu()

def exit_program():
    print("Shutting down...")
    quit()

main_menu()