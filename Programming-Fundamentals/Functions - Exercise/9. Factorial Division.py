def factorial(num1):
    sum_num = 1
    if num1 > 0:

        for num in range(num1, 0, -1):
            sum_num *= num

    return sum_num


def factorial_division(num1, num2):
    return num1 // num2


first_number = int(input())
second_number = int(input())
f1 = factorial(first_number)
f2 = factorial(second_number)
print(f"{factorial_division(f1,f2):.2f}")
