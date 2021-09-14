number_line = int(input())
sum = 0
for line in range(number_line):
    character = input()
    character_in_sum = ord(character)
    sum += character_in_sum

print(f"The sum equals: {sum}")
