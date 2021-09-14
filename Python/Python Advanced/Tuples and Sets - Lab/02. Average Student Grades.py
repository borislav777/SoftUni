def input_to_list(lines):
    l = []
    for _ in range(lines):
        l.append(input())
    return l


def avg(values):
    return sum(values) / len(values)


n = int(input())
data = input_to_list(n)
students = {}
for value in data:
    student, grade = value.split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for student, grades in students.items():
    avg_grade = avg(grades)
    print(f"{student} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg_grade:.2f})")
