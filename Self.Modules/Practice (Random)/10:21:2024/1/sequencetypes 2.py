'''
Working with Lists and Strings
Write a program that asks for a sentence as input, 
then splits it into words and stores each word in a list. 
Print the list of words and their lengths. 
(Prompt: How does knowing sequence types like lists and strings 
allow for more efficient data manipulation in Python?)

'''

def word_list(sentence):
    words = list(map(str,sentence.split(' ')))
    return words

def word_length (sentence):
    words = list(map(str,sentence.split(' ')))
    wordlength = []
    for word in words:
        wordlength.append(len(word))
    return wordlength

sentence = input("Enter a sentence: ").strip('.')
words = word_list(sentence)
wordlength = word_length(sentence)

for i in range(len(wordlength)):
    print (words[i], end = ": ")
    print(wordlength[i], end= "")
    print()