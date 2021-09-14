def input_to_list(lines):
    l = []
    for _ in range(lines):
        l.append(input())
    return l


number_lines = int(input())
data = input_to_list(number_lines)
names = set()
for name in data:
    names.add(name)
for el in names:
    print(el)
