'''
Question 2: 
Create a program that asks the user for their age 
and checks if they are eligible to vote (age >= 18), 
eligible for senior discounts (age >= 65), 
or if they are underage using elif statements.
'''

age = input("Please enter your age: ")

if not age.isalpha():
    age = int(age)
    if age >0:
        if age >= 65:
            print("You are eligible to vote and eligible for senior discounts!")
        elif age >= 18:
            print("You are eligible to vote!")
        if age < 18:
            print("You are too young to vote.")
    else:
        print("Age is invalid.")
else:
    print("Invalid format")

