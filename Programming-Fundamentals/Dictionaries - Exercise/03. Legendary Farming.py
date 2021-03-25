materials = input()
legendary_items = {'fragments': 0, 'motes': 0, 'shards': 0}
win = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
jam = {}
is_win = False
while materials:
    line = materials.split()
    for index in range(0, len(line), 2):
        key = line[index + 1].lower()
        value = int(line[index])
        if key in legendary_items:
            legendary_items[key] += value
            for key, value in legendary_items.items():
                if legendary_items[key] >= 250:
                    print(f"{win[key]} obtained!")
                    legendary_items[key] -= 250
                    is_win = True
                    break
        else:
            if key in jam:
                jam[key] += value
            else:
                jam[key] = value

        if is_win:
            break

    if is_win:
        break

    materials = input()

for key, value in sorted(legendary_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value}")
for key, value in sorted(jam.items(), key=lambda x: (x[0])):
    print(f"{key}: {value}")
