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

        pick_up_action = PickUp(self.player, self.sword)

        self.assertEqual(pick_up_action.obj, self.sword)
        self.assertEqual(pick_up_action.subj, self.player)

        pick_up_action.pick_up()

        self.assertEqual(self.player.get_inventory(), ["sword"])

    def test_lookat(self):

        look_at_sword_action = LookAt(self.player, self.sword)
        look_at_rome_action = LookAt(self.player, self.rome)

        self.assertEqual(look_at_sword_action.look_at(), "ouch it's sharp!")
        self.assertEqual(look_at_rome_action.look_at(), "the pizza is good here")

    def test_use(self):

        use_action = Use(self.player, self.sword)
        use_action.use()
        self.assertEqual(self.player.equipped, self.sword)

    def test_move(self):

        move_north_action = Move(self.player, self.london)

        self.assertEqual(self.player.current_location, self.rome)

        move_north_action.move()

        self.assertEqual(self.player.current_location, self.london)





