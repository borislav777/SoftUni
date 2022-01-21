from unittest import TestCase, main

from project.rooms.room import Room
from project.people.child import Child
from project.appliances.fridge import Fridge


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Johson", 1800, 4)

    def test_init(self):
        self.assertEqual("Johson", self.room.family_name)
        self.assertEqual(1800, self.room.budget)
        self.assertEqual(4, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_set_expenses(self):
        self.room.expenses = 20
        self.assertEqual(20, self.room.expenses)

    def test_set_expenses_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -5

        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses_with_children(self):
        fridge = [Fridge()]
        child = [Child(2, 1, 2, 3)]
        self.room.calculate_expenses(fridge, child)
        self.assertEqual(276, self.room.expenses)

    def test_calculate_expenses_without_children(self):
        fridge = [Fridge()]

        self.room.calculate_expenses(fridge)
        self.assertEqual(36, self.room.expenses)


if __name__ == "__main__":
    main()
