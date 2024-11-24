def reverse_vowels(s):
    vowels =  "aeiou"
    s_vowels = []
    for char in s:
        if char in vowels:
            s_vowels.append(char)
        else: 
            pass
    s_vowels = s_vowels[::-1]
    result = []
    vowel_index = 0
    for char in s:
        if char in vowels:
            result.append(s_vowels[vowel_index])
            vowel_index += 1
        else:
            result.append(char)
    return ''.join(result)
            

s = input("Please enter a string: ")
reversed_s = reverse_vowels(s)
print(reversed_s)