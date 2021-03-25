number_line = int(input())
char_1 = []
last_symbol = ""
for line in range(number_line):
    symbols = input()
    char_1.append(symbols)
    if symbols == "(" and last_symbol == "(":
        break
    elif symbols == "(" or symbols == ")":
        last_symbol = symbols

if char_1.count("(") == char_1.count(")"):
    print("BALANCED")
else:
    print("UNBALANCED")
