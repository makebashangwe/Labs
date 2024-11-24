for i in range(1,51):
    if i <=1:
        continue
    if i == 2:
        print(i)
    elif i == 3:
        print(i)
        continue
    elif i % 2 == 0 or i % 3 ==0:
        continue
    else:
        print(i)


n = int(input("Enter a number: "))
counter = 0
numbers = []
while counter < n + 1:
    numbers.append(counter)
    counter += 1
print(sum(numbers))