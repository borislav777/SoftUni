import re

data = input()
pattern = r"www\.[A-Za-z0-9-]+(\.[a-z ]+)+"
valids = []
while data:
    result = [obj.group() for obj in re.finditer(pattern, data)]
    valids.extend(result)

    data = input()
print('\n'.join(valids))
