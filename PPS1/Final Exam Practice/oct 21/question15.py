'''
Question 2: Write a Python method that uses recursion to calculate the nth 
Fibonacci number.

'''

def fibonacci ():
    fibonacci_list = [0,1]
    for i in range(1,10):
        if i>1:
            fibonacci_list.append((fibonacci_list[i-1])+(fibonacci_list[i-2]))
    return print(fibonacci_list)

fibonacci()
        
'''
def fibonacci(n):
    if n <= 0:
        return 0  # Fibonacci(0) is 0
    elif n == 1:
        return 1  # Fibonacci(1) is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage:
n = int(input("Enter the value of n to get the nth Fibonacci number: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")

    '''