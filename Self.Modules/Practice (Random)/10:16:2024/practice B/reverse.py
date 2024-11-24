def reverse_tuple(tup_list):
    reverse_tup = tup_list[::-1]
    return reverse_tup

reg_tup = input('Enter a list/tuple: ').split(',')
tup_list = tuple(map(str,reg_tup))
result = reverse_tuple(tup_list)
print(result)