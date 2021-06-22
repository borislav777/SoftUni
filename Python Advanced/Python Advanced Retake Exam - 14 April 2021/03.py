def flights(*args):
    destination_flights = {}
    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            return destination_flights
        elif isinstance(args[i], str):
            if args[i] not in destination_flights:
                destination_flights[args[i]] = int(args[i + 1])
            else:
                destination_flights[args[i]] += int(args[i + 1])


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
