'''
Symbol Practice with For Loops
1. Triangle of Asterisks
Write a program that prints a triangle of asterisks (*). The number of rows should be determined by user input.

Example: If the user enters 5, it should print:

*
**
***
****
*****
'''
n = int(input())
stars = "*"
spaces = "-"

for row in range(n):
    for column in range(row+1):
        print(stars, end='')
    print()