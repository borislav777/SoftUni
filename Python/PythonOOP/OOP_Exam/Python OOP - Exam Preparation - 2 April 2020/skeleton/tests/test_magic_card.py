from unittest import TestCase, main

from project.card.magic_card import MagicCard



class TestAdvanced(TestCase):

    def test_init(self):
        card = MagicCard("Exodia")
        self.assertEqual("Exodia", card.name)
        self.assertEqual(5, card.damage_points)
        self.assertEqual(80, card.health_points)


if __name__ == "__main__":
    main()
