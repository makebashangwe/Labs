while True:
    try:
        n = int(input("Input a number: " ))
        break
    except ValueError:
        print("NUMBERS ONLY!")

grid = []
for row in range(n):
    grid.append([0]*n)

for row in grid:
    print(row)