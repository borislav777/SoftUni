coins = float(input())
count_coins = 0
coins =int(coins* 100)
while coins > 1:
    count_coins += coins // 200
    coins = coins % 200
    count_coins += coins // 100
    coins = coins % 100
    count_coins += coins // 50
    coins = coins % 50
    count_coins += coins // 20
    coins = coins % 20
    count_coins += coins // 10
    coins = coins % 10
    count_coins += coins // 5
    coins = coins % 5
    count_coins += coins // 2
    coins = coins % 2

if coins == 1:
    count_coins += 1
print(int(count_coins))
