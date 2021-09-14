def flights(*args, destination_flights={}):
    if args[0] == "Finish":
        return destination_flights
    elif isinstance(args[0], str):
        if args[0] not in destination_flights:
            destination_flights[args[0]] = int(args[1])
        else:
            destination_flights[args[0]] += int(args[1])
    flights(*args[1:], destination_flights)
    return destination_flights


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

