number_of_competition = int(input())
total_money = 0

count_win_competiton = 0
count_lose_competiton = 0

is_win = False
for competition in range(number_of_competition):
    command = input()
    day_money = 0
    count_win = 0
    count_lost = 0
    while command != "Finish":

        result = input()
        if result == "win":
            day_money += 20
            count_win += 1
        else:
            count_lost += 1
        command = input()
    if count_win > count_lost:
        count_win_competiton += 1
        day_money = day_money + day_money * 0.10
    else:
        count_lose_competiton += 1

    total_money += day_money

if count_win_competiton > count_lose_competiton:
    total_money = total_money + total_money * 0.20
    is_win = True
if is_win:
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
