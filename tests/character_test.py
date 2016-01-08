import unittest

from character import *
from item import *


class TestPlayer(unittest.TestCase):

    player = Player("test player", "i'm a test player", 50, 100)

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


class TestEnemy(unittest.TestCase):

    enemy = Enemy("test enemy", "grr i'm a test enemy", 25, 50)

    def test_new_enemy(self):

        self.assertTrue(self.enemy.can_fight)
        self.assertIsInstance(self.enemy, Character)








