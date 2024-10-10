''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
LAB 3
'''
hrs = 0
qualityPts = 0
GPA = 0.0

Course1Hr = int(input("Course 1 hours: "))
Course1 = int(input("Grade for course 1: "))
Course1q = int(Course1Hr * Course1)

Course2Hr = int(input("Course 2 hours: "))
Course2 = int(input("Grade for course 2: "))
Course2q = int(Course2Hr * Course2)

Course3Hr = int(input("Course 3 hours: "))
Course3 = int(input("Grade for course 3: "))
Course3q = int(Course3Hr * Course3)

Course4Hr = int(input("Course 4 hours: "))
Course4 = int(input("Grade for course 4: "))
Course4q = int(Course4Hr * Course4)

totalHours = int(Course1Hr + Course2Hr + Course3Hr + Course4Hr)
print(f"Total hours: {totalHours}")


qualityPts = int(Course1q + Course2q + Course3q + Course4q)
print(f"Total quality points: {qualityPts}")

GPA = float(qualityPts / totalHours)
print(f"Your GPA for this semester is {round(GPA,2)}")

