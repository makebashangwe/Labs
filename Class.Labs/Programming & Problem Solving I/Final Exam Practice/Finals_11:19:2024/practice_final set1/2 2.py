while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Enter a number.")
counter = 0
result = 0
while counter < n:
    counter += 1
    result += counter
print(result)
