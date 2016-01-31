import unittest

from character import *
from item import *
from location import *
from verb import *
from parse import *


class VerbTest(unittest.TestCase):
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    player = Player("hero", "i'm so brave", 100)
    front_gate = Location("Front gate", "You're outside the front gate of town. A town guard is in front of it and a rock is on the floor nearby.")
    main_street = Location("Main street", "The main street of town")
    guard = Npc("guard", "He's standing in front of the town gate. Looks angry...")
    front_gate.add_path({"north": main_street})
    front_gate.add_character(player)
    player.set_location(front_gate)
    front_gate.add_item(sword)
    front_gate.add_character(guard)
    front_gate.add_path({"north": main_street})

    def test_pickup(self):

        PickUp(self.player, self.sword)

        self.assertEqual(self.player.get_inventory(), ["sword"])

    def test_lookat(self):

        parser = Parser(self.player, self.front_gate)

        look_item_action = parser.parse("lookat sword")
        look_char_action = parser.parse("lookat guard")
        look_path_action = parser.parse("look north")

        self.assertEqual(look_item_action.obj, self.sword)
        self.assertEqual(look_char_action.obj, self.guard)
        self.assertEqual(look_path_action.obj, self.front_gate.paths.get('north'))

    def test_move(self):
        self.main_street.travelable = True
        self.assertEqual(self.player.current_location, self.front_gate)

        Move(self.player, self.main_street)

        self.assertEqual(self.player.current_location, self.main_street)





