password = input()

command = input()

while not command == "Done":
    split_command = command.split()
    if split_command[0] == "TakeOdd":
        password = password[1:len(password):2]
        print(password)
    elif split_command[0] == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif split_command[0] == "Substitute":
        substring = split_command[1]
        substitute = split_command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {password}")
