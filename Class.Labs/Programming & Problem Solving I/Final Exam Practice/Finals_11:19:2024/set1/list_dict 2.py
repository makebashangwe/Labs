dict = {"apple":3,"banana":5,"cherry":2}

def update_dict():
    fruit = input("Please enter a name of the fruit you'd like to update: \n")
    quantity = int(input("Please enter the number you'd like to update to: \n"))
    if fruit in dict:
        dict.update({fruit : quantity})
        print("Successfully updated")
    else:
        print("Invalid key.")

def print_dict():
    for i,item in enumerate(dict.items()):
        print(f"{i+1}. {item}")

update_dict()
print_dict()
