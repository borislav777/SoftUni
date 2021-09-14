import re

text = input()
pattern = r"(::|\*\*)[A-Z]([a-z]+){2}\1"
cool_emoji = []
threshold = [int(num) for num in re.findall("\\d", text)]
cool_threshold = 1
for num in threshold:
    cool_threshold *= num
emojies = [obj.group() for obj in re.finditer(pattern, text)]
for emoji in emojies:
    sum_emoji = 0
    for char1 in emoji:
        if not char1 == ":" and not char1 == "*":
            sum_emoji += ord(char1)
    if sum_emoji >= cool_threshold:
        cool_emoji.append(emoji)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojies)} emojis found in the text. The cool ones are:")
if cool_emoji:
    print('\n'.join(cool_emoji))
