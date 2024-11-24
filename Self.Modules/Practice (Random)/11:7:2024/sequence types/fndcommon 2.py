def find_common_elements(array1, array2):
    array3 = []
    for i in range(len(array1)):
        if array1[i] in array2:
            array3.append(array1[i])
    return array3

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(array1, array2)
print(common_elements)  # Output: [3, 4, 5]
