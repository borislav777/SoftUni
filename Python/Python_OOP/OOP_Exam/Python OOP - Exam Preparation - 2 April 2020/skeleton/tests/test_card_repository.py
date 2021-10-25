from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):
    def setUp(self):
        self.cr = CardRepository()

    def test_init(self):
        self.assertEqual(0, self.cr.count)
        self.assertEqual([], self.cr.cards)

    def test_add(self):
        card = MagicCard("Exodia")
        self.cr.add(card)
        self.assertIn(card, self.cr.cards)
        self.assertEqual(1, self.cr.count)

    def test_add_raises(self):
        card = MagicCard("Exodia")
        self.cr.add(card)
        self.assertIn(card, self.cr.cards)
        with self.assertRaises(ValueError) as ex:
            self.cr.add(card)

        self.assertEqual("Card Exodia already exists!", str(ex.exception))

    def test_remove(self):
        card = MagicCard("Exodia")
        self.cr.cards.append(card)
        self.cr.count = 1
        self.cr.remove("Exodia")
        self.assertEqual([], self.cr.cards)
        self.assertEqual(0, self.cr.count)

    def test_remove_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cr.remove("")

        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_find(self):
        card = MagicCard("Exodia")
        self.cr.add(card)
        result = self.cr.find("Exodia")
        self.assertEqual(card, result)


if __name__ == "__main__":
    main()
