dict = {"Alice": 85, "Bob": 78, "Charlie": 92}

def new_student(name, grade = 0):
    dict[name] = grade

def update_student(name, grade = 0):
    dict.update({name: grade})

def print_grades():
    for name, grade in dict.items():
        print(f"{name.capitalize()}: {grade}%")

print_grades()
new_student("Diana", 88)
update_student("Bob", 82)

print()
print("New grades: ")
print_grades()


