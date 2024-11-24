numbers = []
for i in range(1,21):
    numbers.append(i)
print(numbers)

print(numbers[:5:])
print(numbers[15::])
print(numbers[::2])

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = -1
    else:
        continue

print(numbers)