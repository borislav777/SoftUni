number_command = int(input())
parking = {}
for _ in range(number_command):
    command = input().split()
    if command[0] == "register":
        user, plate_number = command[1], command[2]
        if user not in parking:

            parking[user] = plate_number
            print(f"{user} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")

    elif command[0] == "unregister":
        user = command[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            parking.pop(user)

for name, car_number in parking.items():
    print(f"{name} => {car_number}")
