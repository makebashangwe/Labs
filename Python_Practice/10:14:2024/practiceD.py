'''Challenge 2: Count Occurrences of an Element
Task: Write a function that takes a list and an element as 
arguments and returns the number of times that element appears 
in the list.
'''

input_list = ['apple', 'banana', 'apple', 'cherry', 'banana']
element = input()
if element in input_list:
    number = input_list.count(element)
print(f"{element}: {number}")
