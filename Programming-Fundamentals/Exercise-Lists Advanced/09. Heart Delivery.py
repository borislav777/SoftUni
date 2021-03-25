neighborhood = [int(num) for num in input().split("@")]
command = input()
position = 0

while not command == "Love!":
    jump = int(command.split()[1])
    position += jump
    if position < len(neighborhood):

        if neighborhood[position] <= 0:
            print(f"Place {position} already had Valentine's day.")
        else:

            neighborhood[position] -= 2
            if neighborhood[position] <= 0:
                print(f"Place {position} has Valentine's day.")
    else:
        position = 0
        if neighborhood[position] <= 0:
            print(f"Place {position} already had Valentine's day.")
        else:

            neighborhood[position] -= 2
            if neighborhood[position] <= 0:
                print(f"Place {position} has Valentine's day.")
    command = input()
print(f"Cupid's last position was {position}.")
counter = 0
for num in neighborhood:
    if num > 0:
        counter += 1

if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
