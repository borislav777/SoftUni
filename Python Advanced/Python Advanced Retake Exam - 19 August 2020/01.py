from collections import deque

customers = deque([int(el) for el in input().split(", ")])
taxis = [int(el) for el in input().split(", ")]
total_time = 0

while customers and taxis:
    curr_customer = customers.popleft()
    curr_taxi = taxis.pop()
    if curr_taxi >= curr_customer:
        total_time += curr_customer

    else:
        customers.appendleft(curr_customer)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
