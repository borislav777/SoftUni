from unittest import TestCase, main

from project.player.advanced import Advanced


class TestAdvanced(TestCase):

    def test_init(self):
        player = Advanced("Bushido")
        self.assertEqual("Bushido", player.username)
        self.assertEqual(250, player.health)
        self.assertEqual([], player.card_repository.cards)


if __name__ == "__main__":
    main()
