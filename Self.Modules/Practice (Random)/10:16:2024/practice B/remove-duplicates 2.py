
s = input("Enter a list: ").split(",")
s_list = list(set(map(int,s)))
s_list.sort()
print(s_list)