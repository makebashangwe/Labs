def avg(nums):
    return (sum(nums)/len(nums))

user = input("Enter a list of numbers: ").strip().split(',')
nums = list(map(int,user))

average = avg(nums)

for num in nums:
    if num > average:
        print(num)
    else:
        continue

