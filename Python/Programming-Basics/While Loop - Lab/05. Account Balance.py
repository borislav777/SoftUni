contribution = input()
total_money = 0
while contribution != "NoMoreMoney":
    money = float(contribution)
    if money <= 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    total_money += money
    contribution = input()

print(f"Total: {total_money:.2f}")
