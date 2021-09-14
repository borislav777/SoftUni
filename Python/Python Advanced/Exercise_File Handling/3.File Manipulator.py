import os


def create_file(file_name):
    with open(file_name, 'w') as new_file:
        return


def add_to_file(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, 'a') as new_file:
            new_line = new_file.write(f"{content}\n")
    else:
        with open(file_name, 'w') as new_file:
            new_line = new_file.write(f"{content}\n")
    return


def replace_string(file_name, old, new):
    try:
        with open(file_name, 'r') as new_file:

            new_line = []
            for line in new_file.readlines():
                new_line.append(line.strip().replace(old, new))

        with open(file_name, 'w') as new_file:
            new_file.write('\n'.join(new_line))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("An error occurred")


command = input()

while not command == "End":
    manipulations = command.split('-')
    manipulation = manipulations[0]
    file = manipulations[1]
    if manipulation == 'Create':
        create_file(file)
    elif manipulation == 'Add':
        curr_content = manipulations[2]
        add_to_file(file, curr_content)
    elif manipulation == "Replace":
        old_string = manipulations[2]
        new_string = manipulations[3]
        replace_string(file, old_string, new_string)
    elif manipulation == "Delete":
        delete_file(file)
    command = input()
