import re

data = input()
pattern = r"\d+"
all_numbers = []
while data:
    numbers = re.findall(pattern, data)
    all_numbers.extend(numbers)

    data = input()
print(*all_numbers)
