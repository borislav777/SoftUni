ages = int(input())
laundry_price = float(input())
price_per_toy = int(input())
money = 0
toys = 0
total_money = 0
for age in range(1, ages + 1):
    if age % 2 == 0:
        money += 10
        total_money += money - 1
    else:
        toys += 1
money_from_toys = toys * price_per_toy
total_money = money_from_toys + total_money
difference = abs(laundry_price - total_money)
if total_money >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
