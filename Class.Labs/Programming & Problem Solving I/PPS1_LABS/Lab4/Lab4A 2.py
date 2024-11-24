''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab 4A
'''

numberGrade = float(input("Enter the score of your exam: "))

if numberGrade <= 64:
    print("Letter Grade is: F")
elif numberGrade > 64 and numberGrade <= 67:
    print("Letter Grade is: D-")
elif numberGrade > 67 and numberGrade <= 70:
    print("Letter Grade is: D")
elif numberGrade > 70 and numberGrade <= 73:
    print("Letter Grade is: D+")
elif numberGrade > 73 and numberGrade <= 76:
    print("Letter Grade is: C-")
elif numberGrade > 76 and numberGrade <= 79:
    print("Letter Grade is: C")
elif numberGrade > 79 and numberGrade <= 82:
    print("Letter Grade is: C+")
elif numberGrade > 82 and numberGrade <= 85:
    print("Letter Grade is: B-")
elif numberGrade > 85 and numberGrade <= 88:
    print("Letter Grade is: B")
elif numberGrade > 88 and numberGrade <= 91:
    print("Letter Grade is: B+")
elif numberGrade > 91 and numberGrade <= 94:
    print("Letter Grade is: A-")
elif numberGrade > 94 and numberGrade <= 97:
    print("Letter Grade is: A")
elif numberGrade > 97 and numberGrade <= 100:
    print("Letter Grade is: A+")
elif numberGrade > 100:
    print("Letter Grade is: A+")
else:
    print("Invalid Input")