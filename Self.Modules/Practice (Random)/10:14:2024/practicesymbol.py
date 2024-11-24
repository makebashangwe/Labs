n = int(input())

triangle = []
spaces = "-"
star = "*"

for row in range(n):
    for column in range (row+1):
        print(star, end="")
    for column in range(n-row-1):
        print(spaces, end="")
    print()


'''

*----
**---
***--
****-
*****
'''
