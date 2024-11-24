
def invert_dict(user_dict):
    inverted_dict = {}
    value = list(user_dict.values())
    keys = list(user_dict.keys())

    for i in range(len(value)):
        inverted_dict[value[i]] = keys[i]

    return inverted_dict

user_dict = {1:'A' , 2:'B' , 3:'C'}

print(invert_dict(user_dict))
