text = input()
message = input()

while not message == "Reveal":
    command = message.split(":|:")
    operation = command[0]
    if operation == "InsertSpace":
        index = int(command[1])
        if index in range(len(text)):
            text = text[:index] + " " + text[index:]
            print(text)

    elif operation == "Reverse":
        substring = command[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            substring = substring[::-1]
            text = text + substring
            print(text)
        else:
            print("error")

    elif operation == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        text = text.replace(substring, replacement)
        print(text)
    message = input()

print(f"You have a new text message: {text}")
