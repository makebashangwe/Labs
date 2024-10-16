'''
Array Practice
4. Sum of Elements in an Array
Write a function that takes an array of integers and returns the sum of the elements.

Example: Input: [1, 2, 3, 4, 5]
Output: 15
'''

num = input().split(',')
arr = []
arr = list(map(int,num))
print(sum(arr))