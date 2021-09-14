def sum_odd_or_even(num):
    even = 0
    odd = 0
    for el in num:
        el_is_int = int(el)
        if el_is_int % 2 == 0:
            even += el_is_int
        else:
            odd += el_is_int
    return odd,even


number = input()
result = sum_odd_or_even(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")
