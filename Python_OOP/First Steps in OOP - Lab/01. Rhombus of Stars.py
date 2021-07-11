def draw_rhombus(n, count):
    for row in range(n - count):
        print(' ', end="")
    for col in range(1, count):
        print('*', end=" ")
    print("*")


n = int(input())

for count in range(1, n):
    draw_rhombus(n, count)
for count in range(n, 0, -1):
    draw_rhombus(n, count)
