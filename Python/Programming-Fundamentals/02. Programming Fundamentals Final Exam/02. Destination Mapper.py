import re

data = input()
pattern = r"(=|/)[A-Z][A-Za-z]{2,}\1"
travel_points = 0
travel_destination = []
destinations = [destination.group() for destination in re.finditer(pattern, data)]
for curr_dest in destinations:
    curr_dest = re.findall("[A-Za-z]+", curr_dest)
    travel_points += len(*curr_dest)
    travel_destination.extend(curr_dest)
print(f"Destinations: {', '.join(travel_destination)}")
print(f"Travel Points: {travel_points}")
