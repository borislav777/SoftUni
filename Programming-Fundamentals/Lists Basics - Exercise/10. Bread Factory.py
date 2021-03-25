events = input().split("|")
energy = 100
coins = 100
is_all_events = True
for event in events:
    current_event, ingredient = event.split("-")
    ingredient = int(ingredient)
    current_energy = 0
    if current_event == "rest":
        if energy + ingredient < 100:
            current_energy = ingredient
            energy += ingredient
        print(f"You gained {current_energy} energy. ")
        print(f"Current energy: {energy}.")
    elif current_event == "order":

        if energy >= 30:
            coins += ingredient
            energy -= 30
            print(f"You earned {ingredient} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= ingredient
        if coins > 0:
            print(f"You bought {current_event}.")

        else:
            is_all_events = False
            print(f"Closed! Cannot afford {current_event}.")
            break
if is_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
