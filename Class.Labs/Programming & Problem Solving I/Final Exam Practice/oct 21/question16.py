def prime_list(nums):
    prime_nums = [num for num in nums if num % 2 != 0]
    return print(prime_nums)

num_input = input("Please enter a list of numbers seperated by commas: ").strip(' ').split(',')
nums = list(map(int,num_input))
prime_list(nums)


'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_list(nums):
    prime_nums = [num for num in nums if is_prime(num)]  # Use is_prime to filter
    return prime_nums  # Return the list of prime numbers

num_input = input("Please enter a list of numbers separated by commas: ").strip().split(',')
nums = list(map(int, num_input))
primes = prime_list(nums)
print("Prime numbers:", primes)  # Print the result
'''