grades = {}

for _ in range(int(input())):
    name = input()
    score = int(input())
    grades[name] = score

all_scores = sorted(set(grades.values()))
highest_score = all_scores[-1]

students =[]

for name,score in grades.items():
    if score == highest_score:
        students.append(name)

students.sort()

for student in students:
    print(student)