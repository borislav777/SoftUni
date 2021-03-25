import re

text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"
matched = re.findall(pattern, text, re.IGNORECASE)
print(len(matched))
