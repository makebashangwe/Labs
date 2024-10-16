grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for num in grid:
    if int(num) % 2 == 0:
        int(num) = 0

print(grid)