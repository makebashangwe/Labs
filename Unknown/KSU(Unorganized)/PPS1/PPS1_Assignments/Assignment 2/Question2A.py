''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
Assignment 2 '''

age = int(input("Enter your age: "))

if age < 12:
    ticket_price = 8
elif age > 12 and age < 17:
    ticket_price = 10
elif age > 18 and age < 64:
    membership = input("Are you a member of the cinema club? (yes/no) ")
    if membership == "yes":
        ticket_price = 12
    else:
        ticket_price = 15
elif age >= 65:
    ticket_price = 10

print(f"Your ticket price is: ${ticket_price}")