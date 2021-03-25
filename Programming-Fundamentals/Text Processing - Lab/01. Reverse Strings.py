word = input()

while not word == "end":
    rev_word = word[::-1]
    print(f"{word} = {rev_word}")
    word = input()
