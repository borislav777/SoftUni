from collections import deque

number_petrol_pumps = int(input())
petrol_pumps = deque([])
for _ in range(number_petrol_pumps):
    petrol_pumps.append(input())

for big_tour in range(number_petrol_pumps):
    tank = 0
    is_valid = True
    for small_tour in range(number_petrol_pumps):
        curr_petrol_pump = petrol_pumps[small_tour]
        petrol, distance = curr_petrol_pump.split()
        petrol = int(petrol)
        distance = int(distance)
        tank += petrol - distance

        if tank < 0:
            petrol_pumps.append(petrol_pumps.popleft())
            is_valid = False
            break
    if is_valid:
        print(big_tour)
        break

