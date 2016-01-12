import unittest

from character import *
from item import *
from location import *
from lexicon import *


class TestPlayer(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    rome = Location("rome", "the pizza is good here")
    london = Location("london", "you're in britain")
    sword = Item("sword", "ouch i'm sharp!")
    shield = Item("shield", "i'm protect you")
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
        self.assertEqual(["sword", "shield"], self.player.get_inventory())

    def test_set_player_name(self):
        self.player.set_player_name("dlt", "Winterforge")
        self.assertEqual("dlt", self.player.name)

    def test_set_location(self):

        self.player.set_location(self.london)
        self.assertEqual(self.london, self.player.current_location)

    def test_process_action(self):

        processed_move_action = self.player.process_action([("verb", "move"), ("path", "north")])
        processed_pick_up_action = self.player.process_action([("verb", "pick"), ("noun", "sword")])
        processed_look_at_action = self.player.process_action([("verb", "look"), ("path", "north")])

        self.assertEqual(processed_move_action, {"move", self.london})
        self.assertEqual(processed_pick_up_action, {"add_item", self.sword})
        self.assertEqual(processed_look_at_action, {"look_at", self.london})

    def test_do_action(self):

        self.player.do_action("move", self.london)
        self.assertEqual(self.player.current_location, self.london)

        self.player.do_action("move", self.rome)
        self.assertEqual(self.player.current_location, self.rome)

        self.player.do_action("add_item", self.sword)
        self.assertTrue(self.sword in self.player.items)


class TestEnemy(unittest.TestCase):

    enemy = Enemy("test enemy", "grr i'm a test enemy", 50)

    def test_new_enemy(self):

        self.assertTrue(self.enemy.can_fight)
        self.assertIsInstance(self.enemy, Character)








