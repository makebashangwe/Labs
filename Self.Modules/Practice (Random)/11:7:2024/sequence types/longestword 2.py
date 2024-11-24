
def find_longest_word(words):
    for i in range(len(words)-1):
        for j in range(len(words)-i-1):
            if len(words[i]) > len(words[i+1]):
                words[j], words[j+1] = words[j+1], words[j]
    return words[0]

words = ["apple", "banana", "cherry", "kiwi"]
longest_word = find_longest_word(words)
print(longest_word)  # Output: "banana"