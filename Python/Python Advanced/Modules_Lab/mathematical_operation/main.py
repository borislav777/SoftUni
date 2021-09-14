from mathematical_operation import *

mapper = {
    '+':  sum_numbers,
    '-':  subtract_numbers,
    '*':  multiply_numbers,
    '/':  divide_numbers,
    '^':  raise_number

}

first_number, sign, second_number = input().split()
first_number = float(first_number)
second_number = float(second_number)
print(mapper[sign](first_number, second_number) if mapper.get(sign) else "Invalid operator")
