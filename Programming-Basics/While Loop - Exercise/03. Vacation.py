needed_money = float(input())
available_money = float(input())

count_days = 0

spend_days = 0

while available_money < needed_money:
    action = input()
    new_money = float(input())
    count_days += 1
    if action == "spend":
        available_money -= new_money

        if available_money < 0:
            available_money = 0
        spend_days += 1
        if spend_days == 5:
            break

    elif action == "save":
        available_money += new_money
        spend_days = 0

if available_money >= needed_money:

    print(f"You saved the money for {count_days} days.")

else:
    print("You can't save the money.")
    print(f"{count_days}")
