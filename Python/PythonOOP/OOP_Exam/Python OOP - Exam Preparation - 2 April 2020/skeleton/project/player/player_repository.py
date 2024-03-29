class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        p = [p for p in self.players if p.username == player.username]
        if p:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        p = self.find(player)
        self.players.remove(p)
        self.count -= 1

    def find(self, username: str):
        p = [p for p in self.players if p.username == username][0]
        return p
