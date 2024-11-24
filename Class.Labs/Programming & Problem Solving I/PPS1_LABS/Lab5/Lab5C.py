''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab5C
'''

please = ""

while please.lower() != "please":
    please = input("If you would like to stop this program, say “please”: ")
    if please.lower() == "please":
        break
print("Program complete")
