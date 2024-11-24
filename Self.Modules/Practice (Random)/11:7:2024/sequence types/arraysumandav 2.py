def sum_and_average(input_array):
    sum_nums = (sum(input_array))
    average = sum_nums/len(input_array)
    return sum_nums, average

input_array = [1, 2, 3, 4, 5]
total_sum, average = sum_and_average(input_array)
print(total_sum, average)  # Output: 15, 3.0