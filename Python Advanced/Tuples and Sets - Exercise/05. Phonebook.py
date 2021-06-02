data = input()
phonebook = {}

while not data.isnumeric():
    name, number = data.split("-")

    phonebook[name] = number

    data = input()
for _ in range(int(data)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")