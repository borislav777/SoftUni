command = input()

count_steps = 0
target = 10000
isTarget = False

while command != "Going home":
    number_steps = int(command)
    count_steps += number_steps
    if count_steps >= target:
        break
    command = input()

if command == "Going home":
    steps = int(input())
    count_steps += steps
if count_steps >= target:
    isTarget = True
difference = abs(target - count_steps)
if isTarget:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")

else:
    print(f"{difference} more steps to reach goal.")
