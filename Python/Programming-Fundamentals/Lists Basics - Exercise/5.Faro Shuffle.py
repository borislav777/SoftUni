text = input().split()
number_shuffle = int(input())

for shuffle in range(number_shuffle):
    half = len(text) // 2
    first_half = text[:half]
    second_half = text[half:]
    new_text = []
    for card in range(half):
        new_text.append(first_half[card])
        new_text.append(second_half[card])

    text = new_text


print(text)