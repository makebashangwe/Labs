'''
pyramid
---*---
--***--
-*****-
*******
'''

n = int(input())
stars = "*"
spaces = "-"

for row in range(n):
    for column in range(n-1-row): #4-1-0 = 3 SPACES for first half
        print(spaces, end="")
    for column in range(2*row+1): #equation to get an odd number, stars
        print(stars, end="")
    for column in range(n-1-row): #end of the star's spaces
        print(spaces, end="")
    print() #next line