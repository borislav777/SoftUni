box_of_clothes = [int(el) for el in input().split()]
capacity = int(input())
number_rack = 1
curr_capacity = 0
while box_of_clothes:
    curr_clothes = box_of_clothes.pop()
    if curr_capacity + curr_clothes > capacity:
        number_rack += 1
        curr_capacity = 0

    curr_capacity += curr_clothes
print(number_rack)
