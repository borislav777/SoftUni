numbers = int(input())
letters = int(input())
for first_symbol in range(1, numbers + 1):
    for second_symbol in range(1, numbers + 1):
        for third_symbol in range(97, 97+letters):
            for four_symbol in range(97, 97+letters):
                for five_symbol in range(1, numbers + 1):
                    if five_symbol > first_symbol and five_symbol > second_symbol:
                        print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(four_symbol)}{five_symbol}",end=" ")
