import re

text = input()
pattern = r"(@|#)[A-Za-z]{3,}\1{2}[A-Za-z]{3,}\1"
word_pairs = [word.group() for word in re.finditer(pattern, text)]
mirror_word = []
for word in word_pairs:
    if word == word[::-1]:
        word = re.findall("[A-Za-z]+", word)
        mirror_word.append(f"{word[0]} <=> {word[1]}")
if word_pairs:
    print(f"{len(word_pairs)} word pairs found!")

else:
    print("No word pairs found!")

if mirror_word:
    print("The mirror words are:")
    print(', '.join(mirror_word))
else:
    print("No mirror words!")
