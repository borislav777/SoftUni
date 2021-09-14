number_rooms = int(input())
chairs_enough = True
free = 0
for room in range(1, number_rooms + 1):
    chairs, people = input().split()
    people = int(people)
    difference = abs(len(chairs) - people)
    if len(chairs) < people:
        chairs_enough = False
        print(f"{difference} more chairs needed in room {room}")
    else:
        free += difference
if chairs_enough:
    print(f"Game On, {free} free chairs left")
