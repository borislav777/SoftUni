text = input()
counter = 0
resources_list = []
resources = {}
while not text == "stop":
    counter += 1
    resources_list.append(text)

    text = input()

for index in range(0, len(resources_list), 2):
    if resources_list[index] not in resources:

        resources[resources_list[index]] = int(resources_list[index + 1])
    else:
        resources[resources_list[index]] += int(resources_list[index + 1])

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
