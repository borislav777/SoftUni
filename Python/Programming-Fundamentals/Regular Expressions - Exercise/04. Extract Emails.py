import re

data = input()
pattern = r"(^|(?<=\s))[a-z0-9]+([\._-][a-z0-9]+)?@[a-z0-9]+([\.-][a-z0-9]+)?([\.-][a-z0-9]+)?\.[a-z]+"
result = [obj.group() for obj in re.finditer(pattern, data)]
print('\n'.join(result))
