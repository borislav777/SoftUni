symbols = input()
print("".join([el for el in symbols if el.isdigit()]))
print("".join([el for el in symbols if el.isalpha()]))
print("".join([el for el in symbols if not el.isalpha() and not el.isdigit()]))

