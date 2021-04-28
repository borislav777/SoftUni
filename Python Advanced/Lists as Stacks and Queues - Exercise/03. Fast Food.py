from collections import deque

food_for_day = int(input())
orders = deque([int(el) for el in input().split()])
print(max(orders))
is_food_enough = True
while orders:
    curr_orders = orders[0]
    if curr_orders <= food_for_day:
        orders.popleft()
        food_for_day -= curr_orders
    else:
        is_food_enough = False
        break
if is_food_enough:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(el) for el in orders])}")
