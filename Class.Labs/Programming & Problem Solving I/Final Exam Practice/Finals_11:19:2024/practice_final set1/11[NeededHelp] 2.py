dict = {}

name_score = input("Please enter your list of names and scores (eg. Alice 85, Billy 90)").split(",")
pairs = list(map(str,name_score))
for pair in pairs:
    try:
        name,score = pair.strip().split(" ")
        dict[name] = int(score)
    except ValueError:
        print("Invalid format.")
    
print(dict)