'''Problem: Reverse Consonants in a String
Write a function that takes a string and reverses only the consonants (non-vowel letters) 
while leaving the vowels and other characters (like punctuation, spaces, etc.) in their original positions.

Steps:
Collect all consonants from the input string.
Reverse the consonants.
Rebuild the string by replacing each consonant with the corresponding reversed consonant while keeping all other characters (vowels, spaces, punctuation) unchanged.
'''

def reverse_consonants(s):
    vowels =  "AEIOUaeiou"
    const_list = [char for char in s if char.isalpha() and char not in vowels]
    const_list = const_list[::-1]

    result = []
    index_list = 0

    for char in s:
        if char.isalpha() and char not in vowels:
            result.append(const_list[index_list])
            index_list+=1
        else:
            result.append(char)
    return ''.join(result)

s = input("please enter string: ")
reversed_const = reverse_consonants(s)
print(reversed_const)