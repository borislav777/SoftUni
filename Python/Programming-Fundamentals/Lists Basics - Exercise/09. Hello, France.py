items = input().split("|")
budget = float(input())
prices = []
profit = 0
for item in items:
    type_item, price = item.split("->")
    price = float(price)
    if type_item == "Clothes" and price <= 50:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            price = price + price * 0.40

            prices.append(price)
    elif type_item == "Shoes" and price <= 35:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            price = price + price * 0.40
            prices.append(price)
    elif type_item == "Accessories" and price <= 20.50:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            price = price + price * 0.40
            prices.append(price)
budget += sum(prices)
for sale in prices:
    print(f"{sale:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
