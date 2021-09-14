fires = input().split("#")
water = int(input())
fire = []
effort = 0
total_fire = 0
for current_fire in fires:
    level, value = current_fire.split("=")
    value = int(value)

    if level == "High " and 81 <= value <= 125:
        if water >= value:
            water -= value
            fire.append(value)
            total_fire += value
            effort += value * 0.25
    elif level == "Medium " and 51 <= value <= 80:
        if water >= value:
            water -= value
            fire.append(value)
            total_fire += value
            effort += value * 0.25
    elif level == "Low " and 1 <= value <= 50:
        if water >= value:
            water -= value
            fire.append(value)
            total_fire += value
            effort += value * 0.25

print("Cells:")
for extinguished_fire in fire:
    print(f"- {extinguished_fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
