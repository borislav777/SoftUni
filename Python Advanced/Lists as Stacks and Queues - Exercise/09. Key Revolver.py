from collections import deque

bullet_price = int(input())
size_gun_barrel = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
value_of_the_intelligence = int(input())
barrel = size_gun_barrel
count_bullet = len(bullets)
while len(bullets) > 0 and len(locks) > 0:
    curr_lock = locks[0]
    curr_bullet = bullets.pop()
    barrel -= 1
    if curr_bullet <= curr_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if barrel <= 0 and bullets:
        barrel = size_gun_barrel
        print("Reloading!")
money_earned = value_of_the_intelligence - ((count_bullet - len(bullets)) * bullet_price)
if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
