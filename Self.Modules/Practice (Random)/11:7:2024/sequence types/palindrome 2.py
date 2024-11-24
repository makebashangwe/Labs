def check_palindrome(input_string):
    if input_string == input_string[::-1]:
        return True
    else:
        return False

input_string = "racecar"
is_palindrome = check_palindrome(input_string)
print(is_palindrome)  # Output: True