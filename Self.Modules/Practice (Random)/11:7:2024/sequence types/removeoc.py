
def remove_char(input_string, char_to_remove):
    result = []
    for char in input_string:
        if char == char_to_remove:
            continue
        else:
            result.append(char)
    return "".join(result)

input_string = "hello world"
char_to_remove = "o"
result = remove_char(input_string, char_to_remove)
print(result)  # Output: "hell wrld"
