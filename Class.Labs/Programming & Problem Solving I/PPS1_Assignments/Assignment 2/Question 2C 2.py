''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
Assignment 2 '''

number = int(input("Enter a number (1-7): "))

match (number):
    case 1:
        print("The day of the week is: Monday.")
    case 2 :
        print("The day of the week is: Tuesday.")
    case 3:
        print("The day of the week is: Wednesday.")
    case 4:
        print("The day of the week is: Thursday.")
    case 5:
        print("The day of the week is: Friday")
    case 6:
        print("The day of the week is: Saturday.")
    case 7:
        print("The day of the week is: Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")

