'''
Question 1: Define a method called is_prime that takes an integer as input 
and returns True if the number is prime and False otherwise.
'''

def isPrime (n):
    if n % 2 == 0:
        return False
    else:
        return True

n = input("Enter a number: ")
if not n.isalpha():
    n = int(n)
    print(isPrime(n))

'''
def is_prime(n):
    if n < 2:  # Check for numbers less than 2
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # Any other even number is not prime
        return False
    # Check for factors from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter a number: "))
    print(is_prime(n))
except ValueError:
    print("Invalid input. Please enter a valid integer.")

    '''