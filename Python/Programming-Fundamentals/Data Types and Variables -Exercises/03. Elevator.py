import math

number_of_people = int(input())
capacity = int(input())

total_courses = math.ceil(number_of_people / capacity)

print(total_courses)
