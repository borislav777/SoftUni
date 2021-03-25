command = input()
products = {}
while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["quantity"] += quantity
        if not price == products[product]["price"]:
            products[product]["price"] = price
    command = input()
for product, price in products.items():
    result = products[product]["quantity"] * products[product]["price"]
    print(f"{product} -> {result:.2f}")