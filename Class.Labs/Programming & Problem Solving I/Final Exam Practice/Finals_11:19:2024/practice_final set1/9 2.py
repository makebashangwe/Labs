n = input("Enter a list of numbers: ").strip().split(",")
while True:
    try:
        nums = set(map(int,n))
        break
    except ValueError:
        print("Enter numbers only.")
        nums = list(nums)
for i in range(1,len(nums)+1):
    print(nums[-i], end=" ")

