number_pour = int(input())
tank_pour = 0
tank_free_space = 255
is_Full = False
for pour in range(number_pour):
    quantities_water = int(input())

    if tank_free_space >= quantities_water:
        tank_free_space -= quantities_water
        tank_pour += quantities_water

    else:
        print("Insufficient capacity!")

print(tank_pour)
