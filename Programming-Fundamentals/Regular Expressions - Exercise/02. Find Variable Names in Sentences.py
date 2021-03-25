import re

data = input()
pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+($|(?=\s))"
names = [name.group() for name in re.finditer(pattern, data)]
print(*names, sep=",")
