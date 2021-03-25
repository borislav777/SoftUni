numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
for number in range(1, numbers + 1):
    value = int(input())
    if value % 2 == 0:
        p1 += 1
    if value % 3 == 0:
        p2 += 1
    if value % 4 == 0:
        p3 += 1
print(f"{p1 / numbers * 100:.2f}%")
print(f"{p2 / numbers * 100:.2f}%")
print(f"{p3 / numbers * 100:.2f}%")
