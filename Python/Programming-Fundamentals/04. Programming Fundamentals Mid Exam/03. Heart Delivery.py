neighborhood = [int(num) for num in input().split("@")]
command = input()
position = 0
while not command == "Love!":
    comm, jump = command.split()
    jump = int(jump)
    position += jump
    if position > len(neighborhood) - 1:
        position = 0

    if neighborhood[position] > 0:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    else:
        print(f"Place {position} already had Valentine's day.")
    command = input()
print(f"Cupid's last position was {position}.")
counter = 0
for house in neighborhood:
    if house > 0:
        counter += 1

if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
