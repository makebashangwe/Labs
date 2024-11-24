while True:
    try:
        num = int(input("How many names would you like to sort: "))
        break
    except ValueError:

        print("Please enter a number.")

def bubblesort(names):
    print("now sorting...")
    for i in range(0,len(names)-1):
        for i in range(0,len(names)-i-1): #inner loop
            if names[i] > names[i+1]:
                names[i], names[i+1] = names[i+1], names[i]
            
    print("Sorted!")
    return names

names = []
number = 0
for i in range(num):
    number = number + 1
    name = input(f'Please enter Name {number}:' )
    names.append(name)

print(bubblesort(names))