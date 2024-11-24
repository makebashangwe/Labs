sentence = input("Enter sentence: ").lower()

char_count = 0
vowels = "aeiou"
changes = []

for char in sentence:
    if char in vowels:
        char_count +=1
        changes.append("*")
    else:
        changes.append(char)
        continue
print(f"There are {char_count} vowels in \"{sentence.capitalize()}\"!")

print("".join(changes))