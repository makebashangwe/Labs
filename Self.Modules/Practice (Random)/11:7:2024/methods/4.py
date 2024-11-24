def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list if n is 0 or negative
    elif n == 1:
        return [0]  # Return [0] if n is 1
    elif n == 2:
        return [0, 1]  # Return the first two Fibonacci numbers if n is 2

    fibonacci = [0, 1]
    for i in range(n - 2):  # Generate the next n-2 numbers
        fibonacci.append(fibonacci[-1] + fibonacci[-2])  # Sum the last two numbers in the list
    return fibonacci

n = 5
print(fibonacci(n))
