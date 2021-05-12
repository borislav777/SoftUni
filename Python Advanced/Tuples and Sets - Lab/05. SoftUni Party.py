def input_to_list(lines):
    l = []
    for _ in range(lines):
        l.append(input())

    return l


number_guest = int(input())

reservations = set(input_to_list(number_guest))
guests = set()

curr_guest = input()
while not curr_guest == "END":
    guests.add(curr_guest)

    curr_guest = input()

reservations = reservations.difference(guests)
regular_guest = set()
vip_guest = set()

for guest in reservations:
    if guest[0].isdigit():
        vip_guest.add(guest)
    else:
        regular_guest.add(guest)
print(len(reservations))
for guest in sorted(vip_guest):
    print(guest)
for guest in sorted(regular_guest):
    print(guest)
