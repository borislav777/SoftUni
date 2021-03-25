def total_price(prod, q):
    if prod == "coffee":
        return 1.50 * q
    elif prod == "water":
        return 1 * q
    elif prod == "coke":
        return 1.40 * q
    elif prod == "snacks":
        return 2 * q


product = input()
quantity = int(input())

result = total_price(product, quantity)
print(f"{result:.2f}")