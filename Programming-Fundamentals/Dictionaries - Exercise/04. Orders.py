data = input()
products = {}

while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = [quantity, price]
    else:
        products[product][0] += quantity
        if not products[product][1] == price:
            products[product][1] = price

    data = input()
for product, li in products.items():
    products[product] = li[0] * li[1]
for product, total_price in products.items():
    print(f"{product} -> {total_price:.2f}")
