from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])
matches = 0
while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    curr_male = males.pop()
    curr_female = females.popleft()

    if curr_male % 25 == 0:
        males.pop()
        females.appendleft(curr_female)

        continue
    if curr_female % 25 == 0:
        females.popleft()
        males.append(curr_male)

        continue

    if curr_male == curr_female:
        matches += 1

    else:

        curr_male -= 2
        males.append(curr_male)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in males][::-1])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
