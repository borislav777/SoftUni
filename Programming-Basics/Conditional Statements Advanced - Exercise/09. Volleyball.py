year = input()
holiday = int(input())
home_weekend = int(input())
year_weekend = 48
sofia_weekend = year_weekend - home_weekend
games_sofia = sofia_weekend * 3 / 4
games_home = home_weekend
games_holiday = holiday * 2 / 3
total_game = games_sofia + games_home + games_holiday
if year == "leap":
    total_game *= 1.15
print(int(total_game))

