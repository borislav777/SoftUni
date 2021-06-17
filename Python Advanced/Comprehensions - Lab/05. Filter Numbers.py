def check_num(n):
    for i in range(2, 11):
        if n % i == 0:
            return True
    return False


start_i = int(input())
end_i = int(input())
print([num for num in range(start_i, end_i + 1) if check_num(num)])
