'''
Question 4: Write a program that calculates the factorial of a given number using a while loop.

'''

n = input("Enter a number")
if not n.isalpha():
    n = int(n)
    complete = False
    result = 1
    while not complete:
        for i in range(1,n+1):
            n = n-1
            result += n * result
        complete = True
        

print(result)

'''
try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        while n > 0:
            result *= n  # Multiply result by n
            n -= 1  # Decrement n
        print(f"The factorial is {result}.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")'''