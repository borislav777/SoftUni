import re

curr_furniture = input()
pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
total_money = 0
names_furniture = []
while not curr_furniture == "Purchase":
    match = re.match(pattern, curr_furniture)
    if match:
        result = match.groupdict()
        total_money += int(result['quantity']) * float(result['price'])
        names_furniture.append(result['furniture'])
    curr_furniture = input()
print("Bought furniture:")
if names_furniture:
    print('\n'.join(names_furniture))
print(f"Total money spend: {total_money:.2f}")
