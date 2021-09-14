first_command = input()
cities = {}
while not first_command == "Sail":
    city, population, gold = first_command.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    first_command = input()
second_command = input()
while not second_command == "End":
    split_command = second_command.split("=>")

    if split_command[0] == 'Plunder':
        people = int(split_command[2])
        gold = int(split_command[3])
        city = split_command[1]

        cities[city]["population"] -= people
        cities[city]["gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
            print(f"{city} has been wiped off the map!")
            cities.pop(city)
    elif split_command[0] == "Prosper":
        gold = int(split_command[2])
        city = split_command[1]
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")

    second_command = input()
print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
filtered_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1]["gold"],kvp[0]))

for city, value in filtered_cities:
    print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
