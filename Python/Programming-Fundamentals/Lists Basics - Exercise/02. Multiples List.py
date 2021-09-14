factor = int(input())
length = int(input())
numbers = []
for multi in range(1, length + 1):
    numbers.append(factor * multi)

print(numbers)
