number_lines = int(input())

water_tank = 0

for line in range(number_lines):
    quantities_water = int(input())
    water_tank += quantities_water
    if water_tank > 255:
        water_tank -= quantities_water
        print("Insufficient capacity!")

print(water_tank)
