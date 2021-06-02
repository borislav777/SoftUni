n = int(input())
chemical_elements = set()

for _ in range(n):

    chemical_elements = chemical_elements.union(set(input().split()))

for element in chemical_elements:
    print(element)