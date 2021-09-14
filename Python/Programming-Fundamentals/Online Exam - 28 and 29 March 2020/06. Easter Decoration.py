number_client = int(input())
total_product = 0
total_money = 0
count_client = 0

for client in range(number_client):
    command = input()
    money = 0
    count_product = 0
    count_client += 1

    while command != "Finish":
        product = command
        if product == "basket":
            money += 1.50

        elif product == "wreath":
            money += 3.80

        elif product == "chocolate bunny":
            money += 7

        total_product += 1
        count_product += 1

        command = input()

    if count_product % 2 == 0:
        money *= 0.80
    total_money += money
    if command == "Finish":
        print(f"You purchased {count_product} items for {money:.2f} leva.")
average_sum = total_money / count_client
print(f"Average bill per client is: {average_sum:.2f} leva.")
