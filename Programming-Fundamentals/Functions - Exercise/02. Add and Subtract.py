def sum_numbers(num1, num2):
    res_sum = num1 + num2
    return res_sum


def subtract(num1, num2):
    res_subtract = num1 - num2
    return res_subtract


def add_and_subtract(num1, num2, num3):
    return subtract(sum_numbers(num1, num2), num3)


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = add_and_subtract(first_number, second_number, third_number)
print(result)
