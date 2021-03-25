number_lines = int(input())
positive_number = []
negative_number = []
count_positive = 0
sum_negative = 0
for numbers in range(number_lines):
    number = int(input())
    if number >= 0:
        positive_number.append(number)
        count_positive += 1
    elif number < 0:
        negative_number.append(number)
        sum_negative+=number
print(positive_number)
print(negative_number)
print(f"Count of positives: {count_positive}. Sum of negatives: {sum_negative}")
