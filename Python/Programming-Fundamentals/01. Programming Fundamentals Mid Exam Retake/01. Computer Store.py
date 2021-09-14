command = input()
total_price = 0
is_valid = True
while not command == "special" and not command == "regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")

    else:
        total_price += price
    command = input()

if total_price > 0:
    taxes = total_price * 0.20
    if command == "special":
        total = (total_price + taxes) * 0.90
    elif command == "regular":
        total = total_price + taxes
else:
    print("Invalid order!")
    is_valid = False

if is_valid:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")
