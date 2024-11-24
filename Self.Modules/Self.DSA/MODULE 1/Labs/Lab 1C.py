print("TASK 1: Binary Search ")
print()
print()

while True:
    try:
        user = input("Enter a list of numbers (seperated by commas): ").strip().split(",")
        arr = list(map(int,user))
        break
    except ValueError:
            print("Please enter numbers only.")

target =  7


while True:
    try:
        middle = int(len(arr)/2)
        break
    except ZeroDivisionError:
        print("Cannot be an empty array. Division by 0 not allowed.")


if arr[middle] > target:
    for i in range(0,middle):
        if arr[i] == target:
            print(f"Found {target} at index {i}.")
            break
elif arr[middle] < target:
    for i in range(middle,len(arr)):
        if arr[i] == target:
            print(f"Found {target} at index {i}.")
            break
elif arr[middle] == target:
    print(f"Found {target} at index {i}")
    
else:
    print(f"{target} does not exist in this list.")
    

print()
print("TASK 2: Two Sum ")
print()
print()



print()
print("TASK 2: Two Sum ")
print()
print()