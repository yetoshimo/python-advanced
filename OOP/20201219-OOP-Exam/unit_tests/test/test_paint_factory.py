from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    __valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def setUp(self):
        self.test_paint_factory = PaintFactory("a", 1000)

    def test_paint_factory_init(self):
        self.assertEqual("a", self.test_paint_factory.name)
        self.assertEqual(1000, self.test_paint_factory.capacity)
        # self.assertEqual(self.__valid_ingredients, self.test_paint_factory.valid_ingredients)
        self.assertEqual({}, self.test_paint_factory.ingredients)

    def test_paint_factory_add_ingredient_invalid_ingredient_expect_type_error(self):
        _invalid_ingredient = "test"
        with self.assertRaises(TypeError) as context:
            self.test_paint_factory.add_ingredient(_invalid_ingredient, 100)
        self.assertEqual(f"Ingredient of type {_invalid_ingredient} not allowed in PaintFactory", str(context.exception))

    def test_paint_factory_add_ingredient_invalid_quantity_expect_value_error(self):
        _invalid_quantity = 1001
        with self.assertRaises(ValueError) as context:
            self.test_paint_factory.add_ingredient("white", _invalid_quantity)
        self.assertEqual(f"Not enough space in factory", str(context.exception))

    def test_paint_factory_add_ingredient_ingredient_type_not_in_ingredients(self):
        self.test_paint_factory.add_ingredient("white", 0)
        self.assertEqual({"white": 0}, self.test_paint_factory.ingredients)

    def test_paint_factory_add_ingredient_ingredient_type_in_ingredients(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertEqual({"white": 200}, self.test_paint_factory.ingredients)

    def test_paint_factory_remove_ingredient_invalid_ingredient_type_expect_key_error(self):
        self.assertNotIn("white", self.test_paint_factory.ingredients)
        with self.assertRaises(KeyError) as context:
            self.test_paint_factory.remove_ingredient("white", 100)
        # self.assertEqual("'No such product in the factory'", str(context.exception))
        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_paint_factory_remove_ingredient_invalid_quantity_expect_value_error(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertGreater(101, self.test_paint_factory.ingredients["white"])
        with self.assertRaises(ValueError) as context:
            self.test_paint_factory.remove_ingredient("white", 101)
        # self.assertEqual("Ingredient quantity cannot be less than zero", str(context.exception))
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test_paint_factory_remove_ingredient_decrements_ingredient_quantity(self):
        self.test_paint_factory.add_ingredient("white", 100)
        self.test_paint_factory.remove_ingredient("white", 50)
        self.assertEqual({"white": 50}, self.test_paint_factory.ingredients)

    def test_paint_factory_property_products_returns_ingredients(self):
        self.assertDictEqual({}, self.test_paint_factory.ingredients)
        self.test_paint_factory.add_ingredient("white", 100)
        self.assertEqual({"white": 100}, self.test_paint_factory.products)


if __name__ == "__main__":
    main()
