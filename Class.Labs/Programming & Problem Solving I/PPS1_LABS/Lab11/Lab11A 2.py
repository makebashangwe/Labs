import math

def allMath(a,b):
    results = ()
    addition = a+b
    subtraction = a-b
    multiplication = a*b
    if b > 0: 
        division = a/b
        floorDivision = a//b
        modulus = a % b
    else:
        division = None
        floorDivision = None
        modulus = None
    power = a**b
    return (addition, subtraction, multiplication, division, floorDivision, modulus, power)

while True:
    try:
        a = int(input("Enter your first number: "))
        b = int(input("Enter your second number: "))
        break
    except ValueError:
        print("Please enter a number.")
print(f"Your resulting tuple is {allMath(a,b)}")
