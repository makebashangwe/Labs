'''
Reverse Triangle of Numbers
Create a program that prints a reverse triangle with numbers,
where the number of rows is determined by user input.

Example: If the user enters 4, it should print:

Copy code
1 1 1 1
2 2 2
3 3
4'''

n = int(input())

for row in range(n):
    for column in range(n-row):
        print(row+1, end=" ")
    print()