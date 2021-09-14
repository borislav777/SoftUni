start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination = 0
is_found = False
for first in range(start_number, end_number + 1):
    for second in range(start_number, end_number + 1):
        combination += 1
        if first + second == magic_number:
            print(f"Combination N:{combination} ({first} + {second} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{combination} combinations - neither equals {magic_number}")
