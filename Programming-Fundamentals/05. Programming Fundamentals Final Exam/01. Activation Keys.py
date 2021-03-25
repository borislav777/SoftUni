text = input()
command = input()

while not command == "Generate":
    split_command = command.split(">>>")
    if split_command[0] == "Contains":
        if split_command[1] in text:
            print(f"{text} contains {split_command[1]}")
        else:
            print("Substring not found!")
    elif split_command[0] == "Flip":
        start_index = int(split_command[2])
        end_index = int(split_command[3])
        if split_command[1] == "Upper":
            new_text = text[start_index:end_index].upper()
            text = text[:start_index] + new_text + text[end_index:]
        elif split_command[1] == "Lower":
            new_text = text[start_index:end_index].lower()
            text = text[:start_index] + new_text + text[end_index:]
        print(text)
    elif split_command[0] == "Slice":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        text = text[:start_index] + text[end_index:]
        print(text)
    command = input()
print(f"Your activation key is: {text}")
