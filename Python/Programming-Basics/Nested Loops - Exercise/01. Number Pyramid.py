number = int(input())
next_number = 1
is_bigger = False
for row in range(1, number + 1):

    for col in range(1, row + 1):
        print(f"{next_number}", end=" ")
        next_number += 1
        if next_number > number:
            is_bigger = True
            break
    if is_bigger:
        break
    print()
