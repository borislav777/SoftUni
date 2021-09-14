n = int(input())
intersections = []
for _ in range(n):
    first, second = input().split("-")
    start_1, stop_1 = [int(el) for el in first.split(",")]
    start_2, stop_2 = [int(el) for el in second.split(",")]
    intersection = range(max(start_1,start_2),min(stop_1,stop_2)+1)
    intersections.append(intersection)

longest = sorted(intersections,key=lambda x: -len(x))[0]

print(f"Longest intersection is [{', '.join([str(el) for el in longest])}] with length {len(longest)}")