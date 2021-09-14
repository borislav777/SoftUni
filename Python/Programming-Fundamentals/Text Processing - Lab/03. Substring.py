searched_word = input()
text = input()

while searched_word in text:
    text = text.replace(searched_word, "")

print(text)
