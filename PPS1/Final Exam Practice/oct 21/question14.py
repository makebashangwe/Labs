'''
Question 1: Create a method find_max that takes a list of numbers as 
input and returns the maximum value using a for loop.

'''

def find_max(nums):
    max_value = 0
    for num in nums:
        if num > max_value:
            max_value = num
    return print(f"The max value is {max_value}.")

num_input = input("Enter a list of numbers seperated by commas: ").strip(' ').split(',')
nums = list(map(int, num_input))
find_max(nums)