def number_grades_to_word_grade(number_grade):
    if 2 <= number_grade <= 2.99:
        return "Fail"
    elif 3 <= number_grade<= 3.49:
        return "Poor"
    elif 3.50 <= number_grade <= 4.49:
        return "Good"
    elif 4.50 <= number_grade <= 5.49:
        return "Very Good"
    elif 5.50 <= number_grade <= 6:
        return "Excellent"


grade = float(input())

print(number_grades_to_word_grade(grade))