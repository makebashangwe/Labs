def traverse_array(arr):
    for i in range(len(arr)):
        print(arr[i])

def sum_of_elements(arr):
    return sum(arr)

def max_min(arr):
    sorted(arr)
    return arr[0], arr[-1]

while True:
    try:
        user = input("Please enter an array of numbers (seperated by commas): ").strip().split(",")
        arr = list(map(int,user))
        break
    except ValueError:
        print("Please enter numbers only.")

traverse_array(arr)

print(f"Sum: {sum_of_elements(arr)}")

min_Arr, max_Arr = max_min(arr)
print(f"Maximum: {max_Arr}\nMinimum: {min_Arr}")
