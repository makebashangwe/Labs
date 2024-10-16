'''
6. Check If an Element Exists in an Array
Write a function that checks whether a given element exists 
in an array. 
Return True if it exists, otherwise False.

Example: Input: array = [10, 20, 30, 40], element = 30
Output: True
'''

num = input().split(',')
arr = []
arr = list(map(int,num))

element = int(input("Please enter the duplicate element: "))
if element in arr: 
    exist = True
    print(f"Exist?: {exist}")

    if arr.count(element) > 1:
        duplicate = True
        print(f"{duplicate}. \n{element} appears {arr.count(element)} times.")
    else:
        duplicate = False
        print(f"{duplicate}.\n{element} appears once.")

if element not in arr:
    duplicate = False
    exist = False
    print(f"{duplicate}. Exists?: {exist}")
