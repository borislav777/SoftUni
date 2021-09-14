destination = input()

while destination != "End":
    needed_money = float(input())
    money = 0

    while money < needed_money:
        save_money = float(input())
        money += save_money
    else:
        print(f"Going to {destination}!")

    destination = input()
