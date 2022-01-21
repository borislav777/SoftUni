class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def filter(list_filter, type_name, msg):
        l = [el for el in list_filter if el.__class__.__name__ == type_name]
        if l:
            return l
        raise IndexError(msg)

    @property
    def food(self):
        return Bunker.filter(self.supplies, "FoodSupply", "There are no food supplies left!")

    @property
    def water(self):
        return Bunker.filter(self.supplies, "WaterSupply", "There are no water supplies left!")

    @property
    def painkillers(self):
        return Bunker.filter(self.medicine, "Painkiller", "There are no painkillers left!")

    @property
    def salves(self):
        return Bunker.filter(self.medicine, "Salves", "There are no salves left!")
        
    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            last_medicine = [m for m in self.medicine if type(m).__name__ == medicine_type][-1]
            last_medicine.apply(survivor)
            self.medicine.remove(last_medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            last_sustain = [s for s in self.supplies if type(s).__name__ == sustenance_type][-1]
            last_sustain.apply(survivor)
            self.supplies.remove(last_sustain)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
        for s in self.survivors:
            self.sustain(s, "FoodSupply")
            self.sustain(s, "WaterSupply")
