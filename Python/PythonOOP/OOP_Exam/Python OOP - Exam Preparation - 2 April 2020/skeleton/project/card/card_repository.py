class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        c = [c for c in self.cards if c.name == card.name]
        if c:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        self.cards.remove(c)
        self.count -= 1

    def find(self, name: str):
        c = [c for c in self.cards if c.name == name][0]
        return c
