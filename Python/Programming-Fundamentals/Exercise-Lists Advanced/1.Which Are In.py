first_line = input().split(", ")
second_line = input().split(", ")
filtered_list = []
for el in first_line:
    for el1 in second_line:
        if el in el1:
            filtered_list.append(el)

print(sorted(set(filtered_list), key=filtered_list.index))
