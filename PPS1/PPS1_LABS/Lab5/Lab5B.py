''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab5B
'''

while True:
    character = "*"
    space = " "

    try:
        integer = int(input("Please enter a value for the size: "))
        if integer >= 0:
            break
        else:
            print("Please enter a value greater than 0.")
    except ValueError:
        print("Please enter a number. ")

print()

print(f"This is the requested {integer}x{integer} box:")
for i in range(integer):
    for j in range(integer):
        print(character, end="")
    print()
print(f"This is the requested right-facing {integer}x{integer} right-triangle:")
for i in range(integer):
    for j in range(i+1):
        print(character, end="")
    print()

print(f"This is the requested left-facing {integer}x{integer} right-triangle:")

for i in range(integer):
    for j in range(i, integer):
        print(' ', end="")
    for j in range(i+1):
        print(character, end="")
    print()