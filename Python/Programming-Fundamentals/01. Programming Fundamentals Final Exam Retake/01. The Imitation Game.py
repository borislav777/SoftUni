message = input()
command = input()
while not command == "Decode":
    operations = command.split("|")
    operation = operations[0]
    if operation == "Move":
        number_letters = int(operations[1])
        message = message[number_letters:] + message[:number_letters]
    elif operation == "Insert":
        index = int(operations[1])
        value = operations[2]
        message = message[:index] + value + message[index:]

    elif operation == "ChangeAll":
        substring = operations[1]
        replacement = operations[2]
        message = message.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {message}")
