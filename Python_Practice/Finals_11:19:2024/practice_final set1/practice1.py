while True:
    try:
        n = int(input("Input a number: " ))
        break
    except ValueError:
        print("NUMBERS ONLY!")

grid = []
for row in range(n):
    grid.append([0]*n)

if n >= 3:
    grid[0][2] = 6
for row in grid:
    print(row)