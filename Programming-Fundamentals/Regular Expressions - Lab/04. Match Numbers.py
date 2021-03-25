import re

data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = [num.group() for num in re.finditer(pattern, data)]
print(*numbers)