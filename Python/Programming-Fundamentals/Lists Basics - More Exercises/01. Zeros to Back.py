numbers = input().split(", ")
new_numbers = []
zero = []
for num in numbers:
    num = int(num)
    if num == 0:
        zero.append(num)
    else:
        new_numbers.append(num)
print(new_numbers+zero)
