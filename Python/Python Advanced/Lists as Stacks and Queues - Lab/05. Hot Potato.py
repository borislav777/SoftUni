from collections import deque

names = input().split()
step = int(input())
kids = deque(names)
while len(kids)>1:
    for i in range(step-1):
        kids.append(kids.popleft())
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")