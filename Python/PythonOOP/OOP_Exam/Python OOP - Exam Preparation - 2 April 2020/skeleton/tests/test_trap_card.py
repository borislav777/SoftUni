from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TestAdvanced(TestCase):

    def test_init(self):
        card = TrapCard("Exodia")
        self.assertEqual("Exodia", card.name)
        self.assertEqual(120, card.damage_points)
        self.assertEqual(5, card.health_points)


if __name__ == "__main__":
    main()