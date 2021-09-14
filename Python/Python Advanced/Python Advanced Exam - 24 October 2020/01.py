jobs = [int(el) for el in input().split(', ')]
cycles = sorted([(i, jobs[i]) for i in range(len(jobs))], key=lambda x: x[1])

searched_i = int(input())
number_cycle = 0
for index, job in cycles:
    number_cycle += job
    if index == searched_i:
        print(number_cycle)
        break
