def add_user(new_d, curr_side, curr_user):
    for side, users in sides.items():
        if curr_user in users:
            return new_d
    if curr_side not in new_d:
        new_d[curr_side] = []
        new_d[curr_side].append(curr_user)
    else:
        if curr_user not in new_d[curr_side]:
            new_d[curr_side].append(curr_user)
    return new_d


def change_side(new_d, curr_side, curr_user):
    for side, users in sides.items():
        if curr_user in users:
            new_d[side].remove(curr_user)
            return add_user(new_d, curr_side, curr_user)
    return add_user(new_d, curr_side, curr_user)

command = input()
sides = {}

while not command == "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        new_d = add_user(sides, force_side, force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        new_d = change_side(sides, force_side, force_user)
        print(f'{force_user} joins the {force_side} side!')

    command = input()

for s, u in sorted(sides.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(u) > 0:

        print(f"Side: {s}, Members: {len(u)}")
        for force_user in sorted(u):
            print(f"! {force_user}")
