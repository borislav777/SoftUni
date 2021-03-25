class Inventory:

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        if self.capacity > len(self.items):
            self.items.append(item)

        return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {abs(self.capacity-len(self.items))}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
