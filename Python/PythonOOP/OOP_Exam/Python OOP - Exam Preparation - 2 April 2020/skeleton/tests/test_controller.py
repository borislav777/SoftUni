from unittest import TestCase, main

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestController(TestCase):
    def setUp(self):
        self.controller = Controller()
        self.player1 = Beginner("Bushido")
        self.player2 = Beginner("Johny")

        self.player1.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                              MagicCard("Some magic card"), TrapCard("Some trap card"),
                                              MagicCard("Some magic card"), TrapCard("Some trap card")]
        self.player2.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                              MagicCard("Some magic card"), TrapCard("Some trap card")]

    def test_init(self):
        self.assertEqual([], self.controller.player_repository.players)
        self.assertEqual([], self.controller.card_repository.cards)

    def test_add_beginner_player(self):
        self.assertEqual([], self.controller.player_repository.players)
        result = self.controller.add_player("Beginner", "Bushido")
        self.assertEqual("Bushido", self.controller.player_repository.players[0].username)
        self.assertEqual("Beginner", type(self.controller.player_repository.players[0]).__name__)
        self.assertEqual(f"Successfully added player of type Beginner with username: Bushido", result)

    def test_add_advanced_player(self):
        self.assertEqual([], self.controller.player_repository.players)
        result = self.controller.add_player("Advanced", "Bushido")
        self.assertEqual("Bushido", self.controller.player_repository.players[0].username)
        self.assertEqual("Advanced", type(self.controller.player_repository.players[0]).__name__)
        self.assertEqual(f"Successfully added player of type Advanced with username: Bushido", result)

    def test_add_card_magic(self):
        self.assertEqual([], self.controller.card_repository.cards)
        result = self.controller.add_card("Magic", "Exodia")
        self.assertEqual("Exodia", self.controller.card_repository.cards[0].name)
        self.assertEqual("MagicCard", type(self.controller.card_repository.cards[0]).__name__)
        self.assertEqual(f"Successfully added card of type MagicCard with name: Exodia", result)

    def test_add_card_trap(self):
        self.assertEqual([], self.controller.card_repository.cards)
        result = self.controller.add_card("Trap", "Exodia")
        self.assertEqual("Exodia", self.controller.card_repository.cards[0].name)
        self.assertEqual("TrapCard", type(self.controller.card_repository.cards[0]).__name__)
        self.assertEqual(f"Successfully added card of type TrapCard with name: Exodia", result)

    def test_add_player_card(self):
        self.controller.player_repository.players = [Advanced("Bushido"), Beginner("Johny")]
        player = [p for p in self.controller.player_repository.players if p.username == "Johny"][0]
        self.controller.card_repository.cards = [MagicCard("Exodia")]
        result = self.controller.add_player_card("Johny", "Exodia")
        self.assertEqual("Exodia", player.card_repository.cards[0].name)
        self.assertEqual(f"Successfully added card: Exodia to user: Johny", result)

    def test_fight(self):
        player1 = Beginner("Bushido")
        player2 = Beginner("Johny")

        player1.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                         MagicCard("Some magic card"), TrapCard("Some trap card"),
                                         MagicCard("Some magic card"), TrapCard("Some trap card")]
        player2.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                         MagicCard("Some magic card"), TrapCard("Some trap card")]
        self.controller.player_repository.players.append(player1)
        self.controller.player_repository.players.append(player2)

        result = self.controller.fight("Bushido", "Johny")
        self.assertEqual(f"Attack user health 215 - Enemy user health 0", result)

    # def test_report(self):
    #     result = f"Username: Bushido - Health: 50 - Cards 6\n"
    #     result += f"### Card: Some magic card - Damage: 5\n"
    #     result += f"### Card: Some trap card - Damage: 120\n"
    #     result += f"### Card: Some magic card - Damage: 5\n"
    #     result += f"### Card: Some trap card - Damage: 120\n"
    #     result += f"### Card: Some magic card - Damage: 5\n"
    #     result += f"### Card: Some trap card - Damage: 120"
    #     func_result = self.controller.report()
    #     self.assertEqual(result, func_result)


if __name__ == "__main__":
    main()
