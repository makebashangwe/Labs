def count_occurences(nums):
    num_occurences = {}            
    for num in nums:
        if num in num_occurences:
            num_occurences[num] += 1
        else:
            num_occurences[num] = 1

    return num_occurences
                


while True:
    try:
        input_nums = input('Enter a list of numbers: ').strip(' ').split(',')
        nums = list(map(int,input_nums))
        break
    except ValueError:
        print("NUMBERS ONLY PLEASE.")

print(count_occurences(nums))
