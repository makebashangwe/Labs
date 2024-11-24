import random
n=3
grid = []
for row in range(n):
    grid.append([random.randint(1,n*n),random.randint(1,n*n),random.randint(1,n*n)])

for row in grid:
    print(row)

even_count = 0
odd_count = 0
counted = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in counted:
            continue
        else:
            if grid[i][j] % 2 == 0:
                even_count +=1
                counted.append(grid[i][j])
            elif grid[i][j] % 2 != 0:
                odd_count +=1
                counted.append(grid[i][j])

print("odd: ", odd_count)
print("even: ", even_count)