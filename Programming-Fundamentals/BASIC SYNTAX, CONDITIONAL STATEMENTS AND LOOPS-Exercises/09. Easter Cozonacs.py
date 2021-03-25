budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price + flour_price * 0.25)*0.25

price_per_cozonac = eggs_price + flour_price + milk_price
colored_eggs = 0
cozonac = 0
while budget >= price_per_cozonac:
    cozonac += 1
    budget -= price_per_cozonac
    colored_eggs += 3
    if cozonac % 3 == 0:
        colored_eggs -= cozonac - 2
print(f"You made {cozonac} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")