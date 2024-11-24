'''
1. Selection Statements (if, if-else, elif)
Question:
Write a Python function evaluate_number(num) that:

Prints "Positive" if the number is greater than 0.
Prints "Zero" if the number is 0.
Prints "Negative" if the number is less than 0.
Follow-Up: After writing it, test with values like -10, 0, and 5.
'''
def evaluation_number(num):
    if num > 0 :
        print(f'{num} is positive.')
    elif num < 0 :
        print(f'{num} is negative')
    elif num == 0:
        print(f'The number is 0. ')
    else:
        print("Invalid input.")


while True:
    try:
        num = float(input("Please enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

evaluation_number(num)