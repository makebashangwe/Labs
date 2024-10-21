'''
Question 2: Write a Python function called calculate_area that takes two arguments: 
the length and width of a rectangle, and returns the area of the rectangle.
'''

def calculate_area (l,w):
    return l*w

l = int(input("Please enter the length: "))
w = int(input("Please enter the width: "))
print(calculate_area(l,w))