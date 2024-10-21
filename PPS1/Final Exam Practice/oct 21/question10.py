'''
Question 3: Create a function named sum_of_squares that takes a list of numbers 
as a parameter and returns the sum of their squares.

'''

def sum_of_squares(nums):
    nums_squared = [num**2 for num in nums]
    
    squared_sum = 0
    for num in nums_squared:
        squared_sum = squared_sum + num
    return squared_sum

nums = []
input_num = input("Please enter a list of numbers seperated by commas: ").strip(' ').split(',')
nums = list(map(int,input_num))
print(sum_of_squares(nums))