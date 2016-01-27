import unittest

from character import *
from item import *
from location import *


class LocationTest(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    rome = Location("rome", "the pizza is good here")
    rome.add_item(sword)
    shield = Armour("shield", "a solid shield to protect you!", 50, 25)

    def test_add_and_get_item(self):
        self.rome.add_item(self.shield)

        self.assertEqual(self.rome.items, [self.sword, self.shield])
        self.assertEqual(self.rome.get_item("shield"), self.shield)

    def test_add_and_get_character(self):
        self.rome.add_character(self.player)

        self.assertEqual(self.rome.characters, [self.player])
        self.assertEqual(self.rome.get_character("hero"), self.player)

    def test_search_objects(self):

        self.assertEqual(self.rome.search_objects("sword"), self.sword)
        self.assertEqual(self.rome.search_objects("hero"), self.player)
        self.assertEqual(self.rome.search_objects("shield"), self.shield)

