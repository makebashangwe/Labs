'''
Makeba Waddy
Assignment 6A
10/22/2024
CSE 1321L
'''

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return (nums)

def count_positive(nums):
    positive_count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > 0:
            positive_count += 1
    return positive_count

def count_negative(nums):
    negative_count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] < 0:
            negative_count += 1
    return negative_count

numbers = input("Please enter a list of numbers: ").strip(' ').split(' ')

nums = list(map(int,numbers)) #can also be a set to remove duplicates

print(f'Sorted List: {bubble_sort(nums)}')
print(f'Positive Numbers: {count_positive(nums)}')
print(f'Negative Numbers: {count_negative(nums)} ')