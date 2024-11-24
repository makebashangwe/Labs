def count_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
    return vowel_count

#test code
print(count_vowels("hello"))  # 2
print(count_vowels("world"))  # 1