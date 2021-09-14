import re


def replace_sep(list_of_words):
    return re.sub(r"[-,\.!?]", '@', list_of_words)


with open('text.txt', 'r') as file:
    lines = file.readlines()
    for line in range(len(lines)):
        if line % 2 == 0:
            curr_line = replace_sep(lines[line])
            print(' '.join(curr_line.strip().split()[::-1]))
