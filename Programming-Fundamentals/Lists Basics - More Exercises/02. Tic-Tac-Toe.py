first_line = input().split()
second_line = input().split()
third_line = input().split()
count_first = 0
count_second = 0
if first_line.count("1") == 3 or second_line.count("1") == 3 or third_line.count("1") == 3:
    count_first += 1
elif first_line.count("2") == 3 or second_line.count("2") == 3 or third_line.count("2") == 3:
    count_second += 1
elif first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
    count_first += 1
elif first_line[0] == "2" and second_line[1] == "2" and third_line[2] == "2":
    count_second += 1
elif first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
    count_first += 1
elif first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2":
    count_second += 1

else:

    for first in range(len(first_line)):
        if first_line[first] == "1" and second_line[first] == "1" and third_line[first] == "1":
            count_first += 1
            break
        elif first_line[first] == "2" and second_line[first] == "2" and third_line[first] == "2":
            count_second += 1
            break

if count_first > count_second:
    print("First player won")
elif count_second > count_first:
    print("Second player won")
else:
    print("Draw!")
