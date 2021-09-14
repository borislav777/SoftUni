class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]

        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.capacity
        room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"
        return result
