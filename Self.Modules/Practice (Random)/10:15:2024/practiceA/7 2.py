'''
Dictionary Practice
7. Count Occurrences of Words in a String
Write a program that takes a string and counts how many 
times each word appears in the string. The program 
should return a dictionary where the keys are words, 
and the values are the counts.

'''

user = input()
split_words = user.split(' ')
words = []
words = list(map(str,split_words))
print(words)

occurances = {}

for word in words:
    occurances[word] = words.count(word)
    
print(occurances)