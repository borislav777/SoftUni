trunk_capacity = float(input())
command = input()
count_suitcase = 0
is_no_space = False
while command != "End":
    suitcase_volume = float(command)

    count_suitcase += 1
    if count_suitcase % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10
    trunk_capacity -= suitcase_volume
    if trunk_capacity < 0:
        is_no_space = True
        count_suitcase -= 1
        print("No more space!")
        break

    command = input()
if command == "End":
    print(f"Congratulations! All suitcases are loaded!")

print(f"Statistic: {count_suitcase} suitcases loaded.")
