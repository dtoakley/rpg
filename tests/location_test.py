import unittest

from character import *
from item import *
from location import *
from parse import *

class LocationTest(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    front_gate = Location("Front gate", "You're outside the front gate of town. A town guard is iun front of it and a rock is on the floor nearby.")
    guard = Npc("guard", "He's standing in front of the town gate. Looks angry...")
    rock = Item("rock", "A small rock. No bigger than your palm.")
    main_street = Location("Main street", "The main street of town")
    shield = Armour("shield", "a solid shield to protect you!", 50, 25)
    front_gate.add_item(sword)
    front_gate.add_item(rock)
    front_gate.add_path({"north": main_street})

    def test_add_and_get_item(self):
        self.front_gate.add_item(self.shield)

        self.assertEqual(self.front_gate.items, [self.sword, self.rock, self.shield])
        self.assertEqual(self.front_gate.get_item("shield"), self.shield)

    def test_add_and_get_character(self):
        self.front_gate.add_character(self.player)

        self.assertEqual(self.front_gate.characters, [self.player])
        self.assertEqual(self.front_gate.get_character("hero"), self.player)

    def test_search_objects(self):

        self.assertEqual(self.front_gate.search_objects("sword"), self.sword)
        self.assertEqual(self.front_gate.search_objects("hero"), self.player)
        self.assertEqual(self.front_gate.search_objects("shield"), self.shield)

    def test_event(self):
        pass
        # self.player.add_item(self.rock)
        # sentence = "use rock"
        # parser = Parser(self.player, self.front_gate)
        # use_action = parser.parse(sentence)
        # self.front_gate.process_event(use_action)
        #
        # self.assertTrue(self.front_gate.can_travel)
        # self.assertFalse(self.rock in self.player.items)









