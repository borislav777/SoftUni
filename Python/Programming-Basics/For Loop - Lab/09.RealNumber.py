import sys
n=int(input())
min=sys.maxsize
max=-sys.maxsize
for number in range(0,n):
    value=int(input())
    if value>max:
        max=value
    if value<min:
        min=value
print(f"Max number: {max}")
print(f"Min number: {min}")


