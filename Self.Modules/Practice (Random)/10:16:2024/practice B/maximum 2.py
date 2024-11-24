
def find_max(nums):
    max_value = 0

    for num in nums:
        if num > max_value:
            max_value = num

    return max_value

numbers = input().split(',')
nums = list(map(int,numbers))
result = find_max(nums)
print(result)