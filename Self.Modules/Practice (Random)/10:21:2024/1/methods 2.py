'''
Writing and Using Functions
Write a function called calculate_area that takes the width and height of a rectangle 
as parameters and returns the area. Write a separate function that prompts the user 
to enter values for width and height, calls calculate_area, and then prints the result.
(Prompt: What’s the benefit of breaking a program into smaller functions?)
'''

def calculateArea (width,height):
    return width * height

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))
area = calculateArea(width,height)

print (area)