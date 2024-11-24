'''3. Methods (definition, parameters, return values)
Question:
Define a method calculate_area that:

Takes in two parameters: width and height.
Returns the area (width * height) if both values are positive numbers.
Returns "Invalid dimensions" if either parameter is 0 or negative.
Follow-Up: Test the method with various inputs like (5, 10), (0, 5), and (-3, 7).
'''

def calculate_area (width, height):
    return width * height

while True:
    try:
        width = float(input('Enter the width: '))
        if width > 0:
           break
    except ValueError:
        print("Enter a valid number. ")

while True:
    try:
        height = float(input('Enter the heght: '))
        if height > 0:
           break
    except ValueError:
        print("Enter a valid number. ")

print(calculate_area(width, height))
