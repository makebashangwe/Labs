arr = [1,2,3,4,5,6,7,8,9]

print("TASK 1: Array Reversal")
print()
print()

print(f"This was the original array: {arr}")

def reverse_array(arr):
    return arr[::-1]

print(f"This is the reversed array: {reverse_array(arr)}")

print()
print("TASK 2: Two Sum ")
print()
print()

print(f"This is the list of numbers: {arr}")

target = 9
print(f"These are the pairs that equal the target ({target}): ")

def twoSum(arr, target):
    pairs2print = []
    pair_values = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] not in pair_values or arr[j] not in pair_values:
                if arr[i]+arr[j] == target:
                        pairs2print.append(f"{arr[i]} + {arr[j]} = {target}")
                        pair_values.append(arr[j])
                        pair_values.append(arr[i])
    for i in range(len(pairs2print)):
        print(pairs2print[i])


twoSum(arr, target)

print()
print("TASK 3: Rotate Array ")
print()
print()

arr2 = [1,2,3,4,5,6,7,8,9]

print(f"This is the list provided: {arr2}")

def rotate_array(arr2,n):
    for i in range(n):
        arr2.append(arr[i])
        arr2.pop(0)
    return arr2

while True:
    try:
        n = int(input("Enter the number of steps you'd like to rotate the list: "))
        break
    except ValueError:
        print("Enter a number please.")

print(rotate_array(arr2,n))



