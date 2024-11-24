user_dict = {}

key = input("Enter words seperated by commas: ")
key = key.strip(' ').split(',')

for word in key:
    user_dict[key.capitalize()] = len(key)

for item in user_dict.items():
    print(item)
