text = input()

counter = 0
words = ["Sand", "Water", "Fish", "Sun"]

for word in words:
    word_upper = word.upper()
    text_upper = text.upper()

    counter += text_upper.count(word_upper)

print(counter)
