''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Assignment3C
'''

num = 1
for row in range(1,6):
    for col in range(1,6):
        if (num % 2):
            print(f"{num}(O)", end=" ")
        else:
            print(f"{num}(E)", end=" ")
        num += 1
    print()

