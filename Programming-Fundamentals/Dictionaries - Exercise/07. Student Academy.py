rows = int(input())
students = {}
for row in range(rows):
    student_name = input()
    new_grade = float(input())
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(new_grade)
filtered_student = {}
for student, grade in students.items():
    avg = sum(grade) / len(grade)
    if avg >= 4.50:
        filtered_student[student] = avg
for student, grade in sorted(filtered_student.items(), key=lambda kvp: -kvp[1]):
    print(f"{student} -> {float(grade):.2f}")
