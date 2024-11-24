''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab5A
'''

print("Please enter 10 numbers and this program will display the largest.")

numbers = []
for i in range (1,11):
    number = int(input(f"Please enter number {i}: "))
    numbers.append(number)


numbers.sort()
print(f"The largest number was {max(numbers)}")