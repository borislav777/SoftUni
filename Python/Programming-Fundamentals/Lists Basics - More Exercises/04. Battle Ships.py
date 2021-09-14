number_lines = int(input())

new = []
counter = 0
for line in range(number_lines):
    number_as_int = []
    number_as_string = input().split()
    for num in number_as_string:
        number_as_int.append(int(num))
    new.append(number_as_int)

attacked_square = input().split()
for attack in attacked_square:
    rows, colum = attack.split("-")
    row = int(rows)
    col = int(colum)
    if new[row][col] > 0:
        new[row][col] -= 1
        if new[row][col] == 0:
            counter += 1

print(counter)
