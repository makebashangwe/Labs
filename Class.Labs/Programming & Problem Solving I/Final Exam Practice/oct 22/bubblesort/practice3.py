
def grade_sort(students):
    n = len(students)
    for i in range(n):
        for j in range(n-i-1):
            if students[j][1] < students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]
    return students

students = [("Liam", 85), ("Olivia", 92), ("Noah", 78), ("Emma", 92), ("Ava", 74), ("Elijah", 85), ("Sophia", 89), ("James", 95), ("Amelia", 78), ("Isabella", 89)]
sorted_scores = grade_sort(students)


print()
print("Top three scores: ")
for i in range(3):
    print(sorted_scores[i])
print()

n = len(sorted_scores)
print("All scores:")
for i in range(n):
    print(sorted_scores[i])

request_grades = int(input("Enter the grade you'd like to request: "))
try:
    print(f"Students with the score {request_grades}% : ")
    requested_students = []
    for score in sorted_scores:
        if request_grades == score[1]:
            requested_students.append(score[0])
        else:
            continue

    if requested_students:
        for student in requested_students:
            print(student)
    else:
        print("No students found with that score.")
except ValueError:
    print("Please enter a number.")