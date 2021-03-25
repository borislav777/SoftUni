number_plants = int(input())
plants = {}
for _ in range(number_plants):
    curr_plant = input()
    plant, rarity = curr_plant.split("<->")
    rarity = int(rarity)
    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants[plant]['rarity'] += rarity

command = input()

while not command == "Exhibition":
    operation = command.split(": ")
    curr_operation = operation[0]
    if curr_operation == "Rate":
        manipulations = operation[1].split(" - ")
        plant = manipulations[0]
        rating = int(manipulations[1])
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print("error")
    elif curr_operation == "Update":
        manipulations = operation[1].split(" - ")
        plant = manipulations[0]
        new_rarity = int(manipulations[1])
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print("error")
    elif curr_operation == "Reset":
        plant = operation[1]
        if plant in plants:
            plants[plant]['rating'].clear()
        else:
            print("error")

    command = input()
for avg in plants.values():
    if avg['rating']:
        avg['rating'] = sum(avg['rating']) / len(avg['rating'])
    else:
        avg['rating'] = 0

print("Plants for the exhibition:")
for plant, values in sorted(plants.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['rating'])):
    print(f"- {plant}; Rarity: {values['rarity']}; Rating: {values['rating']:.2f}")
