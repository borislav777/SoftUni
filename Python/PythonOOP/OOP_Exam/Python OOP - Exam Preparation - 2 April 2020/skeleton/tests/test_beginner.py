from unittest import TestCase, main


from project.player.beginner import Beginner


class TestAdvanced(TestCase):

    def test_init(self):
        player = Beginner("Bushido")
        self.assertEqual("Bushido", player.username)
        self.assertEqual(50, player.health)
        self.assertEqual([], player.card_repository.cards)


if __name__ == "__main__":
    main()