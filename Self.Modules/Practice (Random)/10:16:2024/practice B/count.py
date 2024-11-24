def count_vowels(s):
    vowels = "AEIOUaeiou"
    vowel_counter = 0

    for char in s:
        if char in vowels:
            vowel_counter += 1
    return vowel_counter

s = input("Type some text: ")
vowel_count  = count_vowels(s)
print(f"Number of vowels: {vowel_count}")
        
