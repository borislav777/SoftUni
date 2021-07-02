def first_half(n):
    for row in range(1, n + 1):
        print()
        for col in range(1, row + 1):
            print(col, end=" ")


def second_half(n):
    for row in range(n - 1, 0, -1):
        print()
        for col in range(1, row + 1):
            print(col, end=" ")


def draw_triangle(n):
    first_half(n)
    second_half(n)
