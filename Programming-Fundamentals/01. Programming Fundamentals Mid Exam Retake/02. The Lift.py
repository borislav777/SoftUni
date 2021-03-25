number_people = int(input())
current_lift = [int(el) for el in input().split()]

for lift in range(len(current_lift)):

    free_spaces = 4 - current_lift[lift]
    if number_people > free_spaces:
        current_lift[lift] += free_spaces
        number_people -= free_spaces
    else:
        current_lift[lift] += number_people
        number_people -= current_lift[lift]
    if number_people == 0:
        break

if len(current_lift) == current_lift.count(4) and number_people > 0:
    print(f"There isn't enough space! {number_people} people in a queue!")
    print(*current_lift)
elif not len(current_lift) == current_lift.count(4) and number_people == 0:
    print("The lift has empty spots!")
    print(*current_lift)

else:
    print(*current_lift)
