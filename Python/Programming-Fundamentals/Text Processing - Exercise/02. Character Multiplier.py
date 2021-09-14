words = input().split()
total = 0
first_word = words[0]
second_word = words[1]

while first_word and second_word:
    result = ord(first_word[0]) * ord(second_word[0])
    total += result
    first_word = first_word[1::]
    second_word = second_word[1::]

if first_word:
    for chr in first_word:
        total += ord(chr)
elif second_word:
    for chr in second_word:
        total += ord(chr)
print(total)