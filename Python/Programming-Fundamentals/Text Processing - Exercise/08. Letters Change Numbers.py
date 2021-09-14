text = input().split()
total = 0
alphabet = {chr(96 + num): num for num in range(1, 27)}

for el in text:
    digit = ""
    result = 0
    if el[0].isupper():
        for char in el:
            if char.isdigit():
                digit += char
        result += int(digit) / alphabet[el[0].lower()]

    elif el[0].islower():
        for char in el:
            if char.isdigit():
                digit += char
        result += int(digit) * alphabet[el[0].lower()]

    if el[-1].isupper():
        total += result - alphabet[el[-1].lower()]
    elif el[-1].islower():
        total += result + alphabet[el[-1].lower()]

print(f"{total:.2f}")