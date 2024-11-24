#size = int(input("Number: "))
size = 5
grid = []

for row in range(size):
    grid.append([0]*size)

for i in range(0,size):
    grid[i][i] = i+1

for row in grid:
    print(row)