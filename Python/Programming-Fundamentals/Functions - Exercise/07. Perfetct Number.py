def is_perfect_number(num1):
    sum_num = 0

    for num in range(1, num1):
        if num1 % num == 0:
            sum_num += num
    if sum_num == num1:
        return True
    return False


number = int(input())
if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")