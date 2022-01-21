from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):
    def setUp(self):
        self.pr = PlayerRepository()

    def test_init(self):
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_add(self):
        player = Beginner("Johny")
        self.pr.add(player)
        self.assertIn(player, self.pr.players)
        self.assertEqual(1, self.pr.count)

    def test_add_raises(self):
        player = Beginner("Johny")
        self.pr.add(player)
        with self.assertRaises(ValueError) as ex:
            self.pr.add(player)
        self.assertEqual("Player Johny already exists!", str(ex.exception))

    def test_remove(self):
        player = Beginner("Johny")
        self.pr.players.append(player)
        self.pr.count = 1
        self.pr.remove("Johny")
        self.assertEqual([], self.pr.players)
        self.assertEqual(0, self.pr.count)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pr.remove("")

        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_find(self):
        player = Beginner("Johny")
        self.pr.add(player)
        result = self.pr.find("Johny")
        self.assertEqual(player, result)

if __name__ == "__main__":
    main()
