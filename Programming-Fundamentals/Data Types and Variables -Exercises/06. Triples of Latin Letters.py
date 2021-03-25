number = int(input())
for first in range(ord("a"), ord("a") + number):
    for second in range(ord("a"), ord("a") + number):
        for third in range(ord("a"), ord("a") + number):
            print(f"{chr(first)}{chr(second)}{chr(third)}")
