    
def insert_index(e, arr):
    while True:
        try:
            e = e.strip('insert ').split(' ')
            command = list(map(int,e))
            arr.insert(command[0], command[1])
            break
        except ValueError:
            print("Please enter a number.")
    return arr

def print_array(arr):
    return print(arr)

def remove_index(e, arr):
    while True:
        try:
            e = e.strip('remove ')
            command = list(map(int,e))
            arr.remove(command[0])
            break
        except ValueError:
            print("Invalid Index.")
    return arr

def append_index(e,arr):
    while True:
        try:
            e = e.strip('append ')
            command = list(map(int,e))
            arr.append(command[0])
            break
        except ValueError:
            print("Please enter a number")
    return arr

def sort_array(arr):
    arr.sort()
    return arr

def pop_array(arr):
    arr.pop()
    return arr

def reverse_array(arr):
    reversed_arr = []
    for i in arr:
        reversed_arr = arr[::-1]
    return reversed_arr

arr = []
reversed_array = reverse_array(arr)

N = int(input())
list_e = []

for i in range(N):
    user = input(" ").strip(' ')
    list_e.append(user)

for i in list_e:
    e = i
    if 'insert' in e:
        insert_index(e,arr)
    if 'print' in e:
        print_array(arr)
    if 'remove' in e:
        remove_index(e,arr)
    if 'append' in e:
        append_index(e,arr)
    if 'sort' in e:
        sort_array(arr)
    if 'pop' in e:
        pop_array(arr)
    if 'reverse' in e:
        reverse_array(arr)
