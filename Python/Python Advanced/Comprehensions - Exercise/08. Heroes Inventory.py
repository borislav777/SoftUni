heroes = {name: {'item': [], 'cost': 0} for name in input().split(", ")}
curr_item = input()

while not curr_item == "End":
    name, item, cost = curr_item.split("-")
    if item not in heroes[name]['item']:
        heroes[name]['item'].append(item)
        heroes[name]['cost'] += int(cost)

    curr_item = input()

print(*[f"{key} -> Items: {len(value['item'])}, Cost: {value['cost']}" for key,value in heroes.items()],sep="\n")