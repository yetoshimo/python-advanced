from unittest import TestCase, main

from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class TestRoom(TestCase):

    def setUp(self):
        self.test_room = Room("test_family", 100, 2)

    def test_room_init_method(self):
        self.assertEqual("test_family", self.test_room.family_name)
        self.assertEqual(100, self.test_room.budget)
        self.assertEqual(2, self.test_room.members_count)
        self.assertEqual([], self.test_room.children)
        self.assertEqual(0, self.test_room.expenses)

    def test_room_negative_expense_expect_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_room.expenses = -100
        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_room_valid_expense(self):
        self.test_room.expenses = 100
        self.assertEqual(100, self.test_room.expenses)

    def test_room_calculate_expenses_no_appliance(self):
        self.test_room.calculate_expenses([])
        self.assertEqual(0, self.test_room.expenses)

    def test_room_calculate_expenses_with_laptop_appliance(self):
        self.test_room.calculate_expenses([Laptop()])
        self.assertEqual(30, self.test_room.expenses)

    def test_room_calculate_expenses_with_laptop_and_tv_appliances(self):
        self.test_room.calculate_expenses([Laptop(), TV()])
        self.assertEqual(75, self.test_room.expenses)


if __name__ == "__main__":
    main()
