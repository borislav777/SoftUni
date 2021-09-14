def input_to_list(lines):
    l = []
    for _ in range(lines):
        l.append(input())

    return l


number_lines = int(input())
data = input_to_list(number_lines)
cars = set()

for car in data:
    direction, car_number = car.split(", ")
    if direction == "IN":
        cars.add(car_number)
    else:

        cars.remove(car_number)
if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
