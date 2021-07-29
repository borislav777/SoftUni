class Equipment:
    EQ_ID = 0

    def __init__(self, name):
        Equipment.EQ_ID += 1
        self.name = name
        self.id = Equipment.EQ_ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.EQ_ID + 1

