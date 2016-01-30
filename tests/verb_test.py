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

    front_gate.add_path({"north": main_street})
    front_gate.add_character(player)
    player.set_location(front_gate)

    def test_pickup(self):

        PickUp(self.player, self.sword)

        self.assertEqual(self.player.get_inventory(), ["sword"])

    def test_lookat(self):
        # TODO add look at tests

        pass

    def test_move(self):
        self.main_street.can_travel = True
        self.assertEqual(self.player.current_location, self.front_gate)

        Move(self.player, self.main_street)

        self.assertEqual(self.player.current_location, self.main_street)





