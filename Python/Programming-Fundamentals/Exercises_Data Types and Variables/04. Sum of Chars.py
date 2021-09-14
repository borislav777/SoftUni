number_line = int(input())
total = 0
for line in range(number_line):
    alphabet_letter = input()
    total += ord(alphabet_letter)
print(f"The sum equals: {total}")

