from collections import deque
from datetime import datetime, timedelta

robots_information = input().split(";")
time = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=1)

robots = []
ready_robots = []
for robot in robots_information:
    data = robot.split("-")
    curr_robot = {}
    curr_robot['name'] = data[0]
    curr_robot['processing_time'] = int(data[1])
    curr_robot['ready'] = time
    robots.append(curr_robot)
    ready_robots.append(curr_robot)

product = input()
products = []

ready_robots = deque(ready_robots)
products = deque(products)
while not product == "End":
    products.append(product)

    product = input()

while len(products) > 0:
    curr_product = products.popleft()
    if not ready_robots:
        for r in robots:
            if time >= r['ready']:
                ready_robots.append(r)
    if ready_robots:
        curr_robot = ready_robots.popleft()

        robot = [el for el in robots if el == curr_robot][0]
        robot['ready'] = time + timedelta(seconds=robot['processing_time'])
        print(f"{curr_robot['name']} - {curr_product} [{time.strftime('%H:%M:%S')}]")
    else:
        products.append(curr_product)
    time = time + timedelta(seconds=1)
