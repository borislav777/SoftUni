text = input()
explosions = 0
result = ""
for index in range(len(text)):
    if text[index] == ">":
        explosions += int(text[index + 1])
        result += text[index]
    elif not explosions == 0:
        explosions -= 1
    else:
        result += text[index]
print(result)
