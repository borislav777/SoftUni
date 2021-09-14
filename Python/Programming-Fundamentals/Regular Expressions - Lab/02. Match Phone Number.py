import re

text = input()
pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
match = [el.group() for el in re.finditer(pattern, text)]
print(', '.join(match))
