
def name_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0,n-i-1):
            if names[j] > names[j+1]:
                names[j],names[j+1] = names[j+1], names[j]
    return names


names = ["Liam", "Olivia", "Noah", "Emma", "Ava", "Elijah", "Sophia", "James", "Amelia", "Isabella"]
sorted_names = name_sort(names)
desired_name = input("Enter a name: ")
if desired_name in sorted_names:
    print(f"{desired_name.capitalize()} is in the list.")
else:
    print(f"{desired_name.capitalize()} is not in the list.")