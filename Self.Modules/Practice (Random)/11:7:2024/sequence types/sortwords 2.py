def sort_words(input_sentence):
    words = input_sentence.lower().split(' ')
    for i in range(len(words)-1):
        for j in range(len(words)-i-1):
            if words[j] > words[j+1]:
                words[j], words[j+1] = words[j+1], words[j]
    return " ".join(words)

input_sentence = "The quick brown fox"
sorted_sentence = sort_words(input_sentence)
print(sorted_sentence)  # Output: "The brown fox quick"