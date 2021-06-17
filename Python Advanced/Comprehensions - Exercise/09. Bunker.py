bunker = {category: {'products': [], 'quantity': 0, 'quality': 0} for category in input().split(", ")}
number_product = int(input())
for _ in range(number_product):
    category, product, attributes = input().split(" - ")
    quantity, quality = [int(el) for attribute in attributes.split(";") for el in attribute.split(':') if el.isdigit()]
    # quality = int(attributes[1].split(";").split(":"))
    if product not in bunker[category]['products']:
        bunker[category]['products'].append(product)
    bunker[category]['quantity'] += quantity
    bunker[category]['quality'] += quality
counter = sum([value['quantity'] for key, value in bunker.items()])
sum_quality = sum([value['quality'] for key, value in bunker.items()])
print(f"Count of items: {counter}")
print(f"Average quality: {sum_quality / len(bunker):.2f}")
print(*[f"{category} -> {', '.join(bunker[category]['products'])}" for category, value in bunker.items()], sep='\n')
