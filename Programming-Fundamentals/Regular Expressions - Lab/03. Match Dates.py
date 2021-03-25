import re

text = input()
pattern = r"\b(?P<day>\d{2})(?P<separator>[/.-])(?P<mouth>[A-Z][a-z]+)\2(?P<year>\d{4})\b"
match = [el.groupdict() for el in re.finditer(pattern, text)]
print('\n'.join([f"Day: {el['day']}, Month: {el['mouth']}, Year: {el['year']}" for el in match]))
# for el in match:
#     print(f"Day: {el['day']}, Month: {el['mouth']}, Year: {el['year']}")
