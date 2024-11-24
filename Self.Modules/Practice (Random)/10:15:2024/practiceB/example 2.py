'''
1. Hollow Square of Asterisks
Create a hollow square of asterisks (*) based on user input for the size of the square.

Example: If the user enters 5, it should print:

]
*****
*   *
*   *
*   *
*****
'''

stars = '*'
spaces = " "
n = 7

for column in range(n): #top
    print(stars, end="")
print()

for row in range(n-2): #middle
    print(stars, end="")
    for column in range(n-2):
        print(spaces, end='')
    print(stars) 

for column in range(n): #bottom
    print(stars, end="")
print()
