text = input()
text_as_list = list(text)
text_index = []

for index in range(len(text_as_list)):
    if text_as_list[index].isupper():
        text_index.append(index)
print(text_index)