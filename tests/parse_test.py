import unittest

from character import *
from item import *
from location import *
from verb import *
from parse import *


class ParseTest(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    rome = Location("rome", "the pizza is good here")
    london = Location("london", "time for some fish and chips")
    shield = Armour("shield", "i'm protect you", 50, 50)
    rome.add_item(sword)
    rome.add_item(shield)
    rome.add_path({"north": london})
    man = Npc("man", "he's carrying a cool walking stick")
    parser = Parser(player, rome)

    def test_parse_pickup(self):

        pickup_sentence = "take sword"
        parsed_pickup = self.parser.parse(pickup_sentence)
        self.assertTrue(isinstance(parsed_pickup, PickUp))
        self.assertEqual(parsed_pickup.subj, self.player)
        self.assertEqual(parsed_pickup.obj, self.sword)

    def test_parse_lookat(self):

        lookat_sentance = "show shield"
        parsed_lookat = self.parser.parse(lookat_sentance)
        self.assertTrue(isinstance(parsed_lookat, LookAt))
        self.assertEqual(parsed_lookat.subj, self.player)
        self.assertEqual(parsed_lookat.obj, self.shield)

    def test_parse_use(self):

        use_sentence = "wield sword"
        parsed_use = self.parser.parse(use_sentence)
        self.assertTrue(isinstance(parsed_use, Use))
        self.assertEqual(parsed_use.subj, self.player)
        self.assertEqual(parsed_use.obj, self.sword)

    def test_parse_move(self):

        move_sentence = "move north"
        parsed_move = self.parser.parse(move_sentence)
        self.assertTrue(isinstance(parsed_move, Move))
        self.assertEqual(parsed_move.subj, self.player)
        self.assertEqual(parsed_move.obj, self.london)




