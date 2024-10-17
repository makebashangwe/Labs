def merge_list(first_list,second_list):
    return first_list + second_list

first_list = input("Enter the first list: ").split(',')
second_list = input("Enter the second list: ").split(',')

joined_list = merge_list(first_list,second_list)

print(joined_list)