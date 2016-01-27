import unittest

from character import *
from item import *
from location import *
from verb import *
from parse import *


class TestPlayer(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    rome = Location("rome", "the pizza is good here")
    london = Location("london", "you're in britain")
    sword = Weapon("sword", "ouch i'm sharp!", 100, 20)
    shield = Armour("shield", "i'm protect you", 50, 50)
    man = Npc("man", "he's carrying a cool walking stick")

    player.set_location(rome)
    rome.add_path({"north": london})
    rome.add_item(sword)
    rome.add_item(shield)
    rome.add_character(man)

    def test_new_player(self):
        self.assertTrue(self.player.player)
        self.assertIsInstance(self.player, Character)

    def test_get_inventory(self):

        self.player.add_item(self.shield)
        self.assertEqual(["shield"], self.player.get_inventory())

    def test_set_player_name(self):
        self.player.set_player_name("dlt", "Winterforge")
        self.assertEqual("dlt", self.player.name)

    def test_set_location(self):

        self.player.set_location(self.london)
        self.assertEqual(self.london, self.player.current_location)


class TestEnemy(unittest.TestCase):

    enemy = Enemy("test enemy", "grr i'm a test enemy", 50)

    def test_new_enemy(self):

        self.assertTrue(self.enemy.can_fight)
        self.assertIsInstance(self.enemy, Character)








