def string_to_words(input_string):
    return list(map(str,input_string.split()))

input_string = "I love programming"
words = string_to_words(input_string)
print(words)  # Output: ['I', 'love', 'programming']
