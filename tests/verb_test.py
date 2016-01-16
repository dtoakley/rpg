import unittest

from character import *
from item import *
from location import *
from verb import *


class VerbTest(unittest.TestCase):
    sword = Item("sword", "ouch it's sharp!")
    player = Player("hero", "i'm so brave", 100)

    def test_pickup(self):

        pick_up_action = PickUp(self.player, self.sword)

        self.assertEqual(pick_up_action.obj, self.sword)
        self.assertEqual(pick_up_action.subj, self.player)

        pick_up_action.pick_up()

        self.assertEqual(self.player.get_inventory(), ["sword"])

    def test_lookat(self):

        look_at_action = LookAt(self.player, self.sword)

        self.assertEqual(look_at_action.obj, self.sword)
        self.assertEqual(look_at_action.subj, self.player)

        self.assertEqual(look_at_action.look_at(), "ouch it's sharp!")


        #TODO get/take
        #TODO use ITEM

        #TODO Look/show


