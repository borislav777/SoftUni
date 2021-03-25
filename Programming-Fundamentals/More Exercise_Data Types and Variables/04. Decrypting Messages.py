key = int(input())
number_lines = int(input())
message = ""
for line in range(number_lines):
    alphabet = input()
    message += chr(ord(alphabet) + key)
print(message)
