message = input().split()

for mess in message:
    number = ""

    for el in mess:

        if el.isdigit():
            number += el

    first_letter = chr(int(number))
    word = first_letter + mess[len(number):]
    word = list(word)
    word[1], word[-1] = word[-1], word[1]

    print(f"{''.join(word)}", end=" ")
