number_cars = int(input())
cars = {}
for _ in range(number_cars):
    curr_car = input()
    car, mileage, fuel = curr_car.split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    if car not in cars:
        cars[car] = {'mileage': mileage, 'fuel': fuel}
    else:
        cars[car] += {'mileage': mileage, 'fuel': fuel}
command = input()

while not command == "Stop":
    operation = command.split(" : ")
    action = operation[0]
    car = operation[1]
    if action == "Drive":
        distance = int(operation[2])
        fuel = int(operation[3])
        if cars[car]['fuel'] >= fuel:
            cars[car]['fuel'] -= fuel
            cars[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car]['mileage'] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)
    elif action == "Refuel":
        fuel = int(operation[2])
        if cars[car]['fuel'] + fuel <= 75:
            cars[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            print(f"{car} refueled with {abs(75 - cars[car]['fuel'])} liters")
            cars[car]['fuel'] = 75


    elif action == "Revert":
        kilometers = int(operation[2])
        cars[car]['mileage'] -= kilometers
        if cars[car]['mileage'] > 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
        else:
            cars[car]['mileage'] = 10000

    command = input()
for car,values in sorted(cars.items(),key=lambda kvp:(-kvp[1]['mileage'],kvp[0])):
    print(f"{car} -> Mileage: {values['mileage']} kms, Fuel in the tank: {values['fuel']} lt.")
