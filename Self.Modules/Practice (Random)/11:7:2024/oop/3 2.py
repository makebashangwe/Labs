class Student:
    def __init__(self, name = "", ID = 0000, grades = []):
        self.name = name
        self.ID = ID
        self.grades = grades

    def average_score (self):
        while True:
            try:
                average = sum(self.grades)/len(self.grades)
                break
            except IndexError:
                print("No grades to add.")
            except ValueError:
                print("Please try again.")
        if average >= 60:
            print(f"Student Passed with an average of {round(average,2)}.")
        elif average < 60:
            print(f"Student failed with an average of {round(average,2)}.")

    def add_grades(self):
        while True:
            try:
                grades_to_add = input("Please enter a list of number grades you'd like to add: ").strip(' ').split(',')
                grades = list(map(int,grades_to_add))
                break
            except ValueError:
                print("Please enter a list of numbers.")
        for grade in grades:
            self.grades.append(grade)
        

        
# Create an instance of the Student class
student1 = Student("John Doe", 1234)

# Add grades
student1.add_grades()  # This will prompt the user to input grades

# Calculate average score
student1.average_score()  # This will print whether the student passed or failed based on the grades

# Print the student's details manually
print(f"Student Name: {student1.name}")
print(f"Student ID: {student1.ID}")
print(f"Student Grades: {student1.grades}")
