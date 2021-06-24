def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for r in range(1, n - 1):
        curr_row = []
        for c in range(len(triangle[r]) + 1):
            if is_valid(r, c - 1, len(triangle)):
                if is_valid(r, c, len(triangle)):
                    curr_row.append(triangle[r][c - 1] + triangle[r][c])
                else:
                    curr_row.append(triangle[r][c - 1])
            else:
                curr_row.append(triangle[r][c])
        triangle.append(curr_row)
    return triangle


print(get_magic_triangle(5))
