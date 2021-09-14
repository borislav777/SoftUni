letters = input()
filtered_letter = []

for i in range(len(letters)):
    if letters[i] not in filtered_letter:
        filtered_letter.append(letters[i])
    elif not letters[i] == filtered_letter[-1]:
        filtered_letter.append(letters[i])

print("".join(filtered_letter))
