from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
is_perfect = False

while len(firework_effects) > 0 and len(explosive_power) > 0:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    curr_effect = firework_effects.popleft()
    curr_power = explosive_power[-1]

    sum_of_ingredients = curr_effect + curr_power
    if sum_of_ingredients % 3 == 0 and sum_of_ingredients % 5 != 0:
        palm_fireworks += 1
        explosive_power.pop()
    elif sum_of_ingredients % 5 == 0 and sum_of_ingredients % 3 != 0:
        willow_fireworks += 1
        explosive_power.pop()

    elif sum_of_ingredients % 5 == 0 and sum_of_ingredients % 3 == 0:
        crossette_fireworks += 1
        explosive_power.pop()

    else:
        curr_effect -= 1
        if curr_effect > 0:
            firework_effects.append(curr_effect)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        is_perfect = True
        break
if is_perfect:
    print("Congrats! You made the perfect firework show!")

else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")

