'''
3. Diamond Pattern
Write a program that prints a diamond shape using asterisks (*). The number of rows for the top half should be based on user input.

Example: If the user enters 3, it should print:

markdown
Copy code
--*--
-***-
*****
-***-
  *

'''
n= 4
stars = "*"
spaces = " "

for row in range(n):
    for column in range(n-row-1): #3-0-1 = 2
        print(spaces, end='')
    for column in range(2*row+1): #1,3,5... row+1 = 1, 2*row+1 = 3, 2*2+1 = 5
        print(stars, end="")
    for column in range(n-row-1): #3-0-1 = 2
        print(spaces, end='')
    print()

for row in range(n-1):
    for column in range(row+1): #0+1=1
        print(spaces, end="")
    for column in range(n-2*row): #3-2*0=3, 3-2=1
        print(stars, end="")
    for column in range(row+1):
        print(spaces, end='')
    print()