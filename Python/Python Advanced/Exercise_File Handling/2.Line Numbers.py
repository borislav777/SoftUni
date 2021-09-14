import re

with open('text.txt', 'r') as file:
    lines = file.readlines()
    new_lines = []
    counter = 1
    for line in lines:
        letter_count = len(re.findall(r'[a-zA-Z]',line))
        marks_count = len(re.findall(r'[-,\.!?\']', line))
        new_lines.append(f"Line {counter}: {line[:-1]} ({letter_count})({marks_count})")
        counter += 1
with open('output.txt', 'w') as output_file:
    output = output_file.writelines('\n'.join(new_lines))
