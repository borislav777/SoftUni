import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = re.findall(pattern, text)
print(' '.join(text))
