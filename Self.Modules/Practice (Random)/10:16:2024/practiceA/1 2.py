def add_and_reverse(nums, n):
    list_nums = list(map(int,nums))
    list_nums.append(n)
    return list_nums[::-1]

nums = input("Please enter a list of numbers: ").split(',')
n = int(input("Please enter the number to add: "))
reverse = add_and_reverse(nums, n)
print(reverse)