'''
Question 1: Write two overloaded methods named area. 
One method should calculate the area of a rectangle (using two parameters 
for length and width), and the other should calculate the area of a circle 
(using one parameter for the radius).
'''
import math

def area_rectangle(l,w):
    return print(l*w)

def area_circle(r):
    return print(math.pi*r**2)

area_rectangle(20,20)
area_circle(20)

'''
Explain the concept of method overloading. 
Why do we use it, and how does Python handle method overloading differently 
compared to other programming languages like Java or C++?
Your implementation demonstrates the concept of method overloading well, as you 
defined two functions with the same name but different parameters.
 However, Python does not natively support method overloading in the same 
 way that languages like Java or C++ do. Instead, you can achieve similar 
 functionality by using default parameters or checking the number of arguments. 
 Below is a corrected version of your code that uses a single area function to 
 handle both cases:

import math

def area(shape, *args):
    if shape == "rectangle":
        if len(args) == 2:
            return args[0] * args[1]  # Area of rectangle
        else:
            return "Invalid number of parameters for rectangle."
    elif shape == "circle":
        if len(args) == 1:
            return math.pi * args[0] ** 2  # Area of circle
        else:
            return "Invalid number of parameters for circle."
    else:
        return "Unknown shape."

# Example usage
print("Area of rectangle:", area("rectangle", 20, 20))
print("Area of circle:", area("circle", 20))

'''

