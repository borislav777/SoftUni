from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
time_for_pass = green_light
cars = deque()
is_valid = True
total_car = 0
while not command == "END":
    if command == "green":
        time_for_pass = green_light
        while time_for_pass > 0 and len(cars) > 0:
            car = cars.popleft()
            time_for_pass -= len(car)
            if time_for_pass >= 0:
                total_car += 1
            else:
                free_window += time_for_pass
                if free_window < 0:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[len(car) + free_window]}.")
                    is_valid = False
                    break
                total_car += 1

        if not is_valid:
            break
    else:
        cars.append(command)
    command = input()

if command == "END":
    print("Everyone is safe.")
    print(f"{total_car} total cars passed the crossroads.")
