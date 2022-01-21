class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([r.expenses + r.room_cost for r in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        pay_result = []
        for family in self.rooms:
            month_consumption = family.expenses + family.room_cost
            if family.budget >= month_consumption:
                family.budget -= month_consumption
                pay_result.append(f"{family.family_name} paid {month_consumption:.2f}$ and have {family.budget:.2f}$ left.")
            else:
                pay_result.append(f"{family.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(family)
        return '\n'.join(pay_result)

    def status(self):
        result = ""
        all_people_in_the_hotel = sum([r.members_count for r in self.rooms])
        result += f"Total population: {all_people_in_the_hotel}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$," \
                      f" Expenses: {room.expenses:.2f}$\n"
            if room.children:
                count = 0
                for child in room.children:
                    count += 1
                    result += f"--- Child {count} monthly cost: {child.cost * 30:.2f}$\n"
            if hasattr(room, "appliances"):
                result += f"--- Appliances monthly cost: " \
                          f"{sum([a.get_monthly_expense() for a in room.appliances]):.2f}$\n"
        return result
