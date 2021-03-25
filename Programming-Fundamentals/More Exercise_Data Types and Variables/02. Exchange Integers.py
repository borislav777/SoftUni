first_number = int(input())
second_number = int(input())

print("Before:")
print(f"a = {first_number}")
print(f"b = {second_number}")
temp = first_number
first_number = second_number
second_number = temp
print("After:")
print(f"a = {first_number}")
print(f"b = {second_number}")
