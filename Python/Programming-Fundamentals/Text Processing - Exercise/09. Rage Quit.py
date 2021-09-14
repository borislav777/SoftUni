text = input()
result = ""

curr_result = ""
for index in range(len(text)):

    if text[index].isdigit():
        digits = ""
        while index < len(text) and text[index].isdigit():
            digits += text[index]
            index += 1

        result += curr_result * int(digits)
        curr_result = ""
    else:
        curr_result += text[index].upper()

unique_symbols = set(result)
print(f"Unique symbols used: {len(unique_symbols)}")
print(result)
