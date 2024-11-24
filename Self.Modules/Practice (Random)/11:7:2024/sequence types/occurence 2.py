def count_char_occurrences(input_string, letter):
    occurence = 0
    for char in input_string:
        if char == letter:
            occurence += 1
        else:
            continue
    return occurence

input_string = "banana"
letter = "a"
count = count_char_occurrences(input_string, letter)
print(count)  # Output: 3