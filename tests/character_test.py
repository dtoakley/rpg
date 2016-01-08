import unittest

from character import *
from item import *
from location import *
from lexicon import *

class TestPlayer(unittest.TestCase):

    player = Player("test player", "i'm a test player", 50, 100)
    location = Location("test location", "a test location")
    item = Item("test item", "a test item")

    def test_new_player(self):
        self.assertTrue(self.player.player)
        self.assertIsInstance(self.player, Character)

    def test_get_inventory(self):
        item = Item("test item", "a test item", 10)
        item2 = Item("test item 2", "another test item", 20)

        self.player.add_item(item)
        self.assertEqual(["test item"], self.player.get_inventory())

        self.player.add_item(item2)
        self.assertEqual(["test item", "test item 2"], self.player.get_inventory())

    def test_set_player_name(self):
        self.player.set_player_name("new name", "game name")
        self.assertEqual("new name", self.player.name)

    def test_set_location(self):

        self.player.set_location(self.location)

        self.assertEqual(self.location, self.player.current_location)

    def test_take_turn(self):
        pass

class TestEnemy(unittest.TestCase):

    enemy = Enemy("test enemy", "grr i'm a test enemy", 25, 50)

    def test_new_enemy(self):

        self.assertTrue(self.enemy.can_fight)
        self.assertIsInstance(self.enemy, Character)








