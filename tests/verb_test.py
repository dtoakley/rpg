import unittest

from character import *
from item import *
from location import *
from verb import *
from parse import *


class VerbTest(unittest.TestCase):
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    player = Player("hero", "i'm so brave", 100)
    rome = Location("rome", "the pizza is good here")
    london = Location("london", "time for fish and chips?")
    rome.add_path({"north": london})
    rome.add_character(player)
    player.set_location(rome)

    def test_pickup(self):

        PickUp(self.player, self.sword)

        self.assertEqual(self.player.get_inventory(), ["sword"])

    def test_lookat(self):
        # TODO add look at tests

        pass

    def test_use(self):

        Use(self.player, self.sword)
        self.assertEqual(self.player.equipped, self.sword)

    def test_move(self):

        self.assertEqual(self.player.current_location, self.rome)

        Move(self.player, self.london)

        self.assertEqual(self.player.current_location, self.london)





