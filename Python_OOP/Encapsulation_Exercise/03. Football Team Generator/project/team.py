class Team:

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        players = [p for p in self.__players if p.name == player.name]
        if players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        players = [p for p in self.__players if p.name == player_name]
        if players:
            self.__players.remove(players[0])
            return players[0]
        return f"Player {player_name} not found"

