number_words = int(input())
word = input()
words = []
filtered_text = []
for _ in range(number_words):
    text = input()
    words.append(text)
for index in range(len(words)):
    if word in words[index]:
        filtered_text.append(words[index])

print(words)
print(filtered_text)



