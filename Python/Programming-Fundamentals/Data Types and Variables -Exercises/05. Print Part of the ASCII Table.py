start_number = int(input())
last_number = int(input())
for character in range(start_number, last_number + 1):
    number_in_character = chr(character)
    print(f"{number_in_character}", end=" ")
