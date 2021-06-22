from collections import deque

orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]
total_pizza_made = 0
while len(orders) > 0 and len(employees) > 0:
    curr_order = orders.popleft()
    if 0 < curr_order <= 10:
        curr_employee = employees.pop()
        if curr_order > curr_employee:
            curr_order -= curr_employee
            total_pizza_made += curr_employee
            if employees:
                while curr_order > 0:
                    curr_employee = employees.pop()
                    total_pizza_made += curr_order
                    curr_order -= curr_order
            else:
                orders.appendleft(curr_order)

        else:
            total_pizza_made += curr_order

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in orders])}")



