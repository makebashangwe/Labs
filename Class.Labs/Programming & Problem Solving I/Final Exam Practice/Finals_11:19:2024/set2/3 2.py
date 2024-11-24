grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
grid[1][1] = 1
print(grid)

for i in range(3):
    grid[i][i] = 9

print(grid)

new_grid = []
n = 3
for row in range(n):
    new_grid.append([])
    for column in range(n):
        new_grid.append([])
    

for row in range(n):
    for col in range(n):
        print(new_grid[col], end = " ")
    print()
