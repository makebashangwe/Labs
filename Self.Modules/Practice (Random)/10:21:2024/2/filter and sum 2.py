'''
List Filtering and Summing
Write a function, filter_and_sum, that takes a list of 
integers and a threshold integer as input. The function 
should return the sum of all numbers in the list that are 
greater than the threshold. (Challenge: Use list comprehension to solve this.)
'''

def filter_and_sum(nums, threshold):
    return sum([num for num in nums if num > threshold])

input_list = input("Enter a list of numbers: ").strip(' ')
input_list = input_list.split(',')

while True:
    try:
        threshold = float(input("Enter the threshold integer: "))
        break
    except ValueError:
        print("Enter a number please.")

nums = list(map(int,input_list))
print(filter_and_sum(nums, threshold))