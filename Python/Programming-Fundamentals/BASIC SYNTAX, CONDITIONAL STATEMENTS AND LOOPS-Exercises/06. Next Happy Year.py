year = int(input())

while True:
    year += 1
    year_as_string = str(year)
    is_happy = True
    for index_1 in range(len(year_as_string)):

        for index_2 in range(len(year_as_string)):
            if index_1 == index_2:
                continue
            if year_as_string[index_1] == year_as_string[index_2]:
                is_happy = False
    if is_happy:
        print(year)
        break
