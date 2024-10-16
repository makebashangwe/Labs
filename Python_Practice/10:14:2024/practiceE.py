'''
Task: Write a function that finds the maximum value in a 2D list 
and returns it.

'''
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row = list(max(grid))
row = row.sort()
print(row[-1])


