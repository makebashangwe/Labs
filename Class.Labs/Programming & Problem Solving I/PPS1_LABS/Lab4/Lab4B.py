''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab 4B
'''

print("Welcome!")
number = float(input("Please input a number: "))

userInput = int(input("""What would you like to do to this number:

0) Get the additive inverse of the number
1) Get the reciprocal of the number
2) Square the number
3) Cube the number
4) Exit the program
"""))

match userInput:
    case 0:
        print(f"The additive inverse of {number} is -{number}")
    case 1:
        if number == 0:
            print("Cannot divide by 0!")
        else:
            print(f"The reciprocal of {number} is {1/number}")
    case 2:
        print(f"The square of {number} is {number**2}")
    case 3:
        print(f"The cube of {number } is {number**3}")
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid input, please try again!")