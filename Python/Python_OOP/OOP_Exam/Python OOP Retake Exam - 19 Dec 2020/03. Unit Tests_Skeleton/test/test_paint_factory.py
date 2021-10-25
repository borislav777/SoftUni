from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.pf = PaintFactory("Anycomp", 100)

    def test_init(self):
        self.assertEqual("Anycomp", self.pf.name)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)
        self.assertEqual({}, self.pf.ingredients)

    def test_add_ingredient_valid_product_type_and_quantity_product_type_exist(self):
        self.pf.ingredients = {"white": 10}
        self.pf.add_ingredient("white", 20)
        self.assertEqual({"white": 30}, self.pf.ingredients)

    def test_add_ingredient_valid_product_type_and_quantity_product_type_not_exist(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient("white", 20)
        self.assertEqual({"white": 20}, self.pf.ingredients)

    def test_add_ingredient_insufficient_capacity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient("white", 150)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_invalid_ingredients_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient("black", 50)

        self.assertEqual(f"Ingredient of type black not allowed in {self.pf.__class__.__name__}", str(ex.exception))

    def test_remove_ingredient_if_ingredient_exist_greater_than_zero(self):
        self.pf.ingredients = {"white": 120}
        self.pf.remove_ingredient("white", 20)
        self.assertEqual({"white": 100}, self.pf.ingredients)

    def test_remove_ingredient_if_ingredient_exist_equal_to__zero(self):
        self.pf.ingredients = {"white": 120}
        self.pf.remove_ingredient("white", 120)
        self.assertEqual({"white": 0}, self.pf.ingredients)

    def test_remove_ingredient_if_ingredient_exist_less_than__zero_raises(self):
        self.pf.ingredients = {"white": 120}
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient("white", 130)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_if_ingredient_not_exist_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient("white", 130)

        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_product_property(self):
        self.pf.ingredients = {"white": 120}
        result = self.pf.products
        self.assertEqual({"white": 120}, result)


if __name__ == "__main__":
    main()
