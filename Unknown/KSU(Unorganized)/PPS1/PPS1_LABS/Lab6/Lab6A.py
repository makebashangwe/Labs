''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab6A
'''
def area(width, height):
    return width * height


def perimeter(width, height):
    return 2 * (width + height)

def IsValid(width, height):
    sum = float(width + height)
    if sum >30:
        print("This is a valid rectangle.")
        return True
    else:
        print("This is an invalid rectangle.")
        return False



play = True

while play == True:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    valid = IsValid(width, height)

    if valid == True:
        rect_area = area(width, height)
        rect_perimeter = perimeter(width, height)
        print(f"The area is: {rect_area}\n"
              f"The perimeter is: {rect_perimeter}")

    playAgain = input("Do you want to enter another width and height (Y/N)?: ").lower()

    if "y" in playAgain:
        play = True
    if "n" in playAgain:
        print("Program Ends")
        play = False