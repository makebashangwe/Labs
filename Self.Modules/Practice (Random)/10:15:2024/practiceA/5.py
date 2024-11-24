'''
5. Find the Maximum Element
Create a function that takes an array of integers and 
returns the maximum value.

Example: Input: [3, 5, 7, 2, 8, -1]
Output: 8
'''

num = input().split(',')
arr = []
arr = list(map(int,num))
max_value = 0
for i in arr:
    if i>max_value:
        max_value = i

print(max_value)


