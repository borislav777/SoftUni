n = int(input())
odd = set()
even = set()
for curr_row in range(1,n+1):
    name = sum([ord(el) for el in input()])
    name_sum = name // curr_row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)
sum_odd = sum(odd)
sum_even = sum(even)
if sum_odd == sum_even:
    odd = odd.union(even)
    print(', '.join([str(el)for el in odd]))
elif sum_odd > sum_even:
    odd = odd.difference(even)
    print(', '.join([str(el)for el in odd]))
else:
    odd = odd.symmetric_difference(even)
    print(', '.join([str(el) for el in odd]))