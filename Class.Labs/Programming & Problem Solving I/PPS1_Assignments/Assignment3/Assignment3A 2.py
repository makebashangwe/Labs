''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Assignment3A
'''

'''Assignment 3A: Pattern Generator
Write a Python program that prompts the user for a positive integer and prints a pyramid pattern
with numbers.
Instructions:
1. Prompt the user for a positive number
2. Print out as many rows as that positive number indicates. For example, if the user enters
4, you'll print out 4 rows of numbers. If the user enters 15, you'll print out 15 rows of
numbers.
3. Each row should be made up of numbers counting from 1 left to right. Each row should
have exactly as many numbers on it as the row number. For example, row 1 will have 1
number, row 4 will have 4 numbers.'''

n = int(input('Enter a positive number: '))
num = 1
for row in range (1,n+1): #counts straight down
    for col in range (1,row+1): #count across
        print(num, " ", end='') #prints the variable, ending to print a new line
        num += 1 #incriments the variable
    print()