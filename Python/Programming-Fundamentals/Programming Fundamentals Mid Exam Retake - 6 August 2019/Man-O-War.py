def is_valid(index, li):
    if index in range(len(li)):
        return True
    return False


def repair(index, health, li):
    if is_valid(index, li):
        if li[index] + health <= maximum_health:
            li[index] += health
        else:
            li[index] = maximum_health

        return li[index]


def check_status(li):
    counter = 0
    for section in li:
        if section < maximum_health * 0.20:
            counter += 1

    return print(f"{counter} sections need repair.")


pirate_ship = [int(num) for num in input().split(">")]
status = [int(num) for num in input().split(">")]
maximum_health = int(input())
command = input()
is_end = False

while not command == "Retire":
    split_comm = command.split()
    if split_comm[0] == "Fire":
        ind = int(split_comm[1])
        dmg = int(split_comm[2])
        if is_valid(ind, status):
            status[ind] -= dmg

            if status[ind] <= 0:
                print("You won! The enemy ship has sunken.")
                is_end = True
                break
    elif split_comm[0] == "Defend":
        s_ind = int(split_comm[1])
        end_ind = int(split_comm[2])
        dmg = int(split_comm[3])
        if is_valid(s_ind, pirate_ship) and is_valid(end_ind, pirate_ship):
            for attack in range(s_ind, end_ind + 1):
                pirate_ship[attack] -= dmg
                if pirate_ship[attack] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_end = True
                    break
    elif split_comm[0] == "Repair":
        ind = int(split_comm[1])
        heal = int(split_comm[2])
        repair(ind, heal, pirate_ship)
    elif split_comm[0] == "Status":
        check_status(pirate_ship)

    command = input()
if not is_end:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(status)}")
