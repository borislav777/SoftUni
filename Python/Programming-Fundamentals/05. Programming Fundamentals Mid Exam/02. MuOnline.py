dungeons = input().split("|")
health = 100
bitcoins = 0
count_room = 0
is_all = True
for dungeon in dungeons:
    command, value = dungeon.split()
    value = int(value)
    count_room += 1
    if command == "potion":

        if value + health <= 100:
            health += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")
        else:
            diff = abs(health - 100)
            health += diff
            print(f"You healed for {diff} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:

            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {count_room}")
            is_all = False
            break
if is_all:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
