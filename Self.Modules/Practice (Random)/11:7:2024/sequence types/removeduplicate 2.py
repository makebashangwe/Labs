def remove_duplicates(input_list):
    return set(input_list)


input_list = [1, 2, 2, 3, 4, 4, 5]
output_list = remove_duplicates(input_list)
print(output_list)  # Output: [1, 2, 3, 4, 5]