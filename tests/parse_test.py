import unittest

from character import *
from item import *
from location import *
from verb import *
from parse import *


class ParseTest(unittest.TestCase):

    player = Player("hero", "i'm so brave", 100)
    front_gate = Location("Front gate", "You're outside the front gate of town. A town guard is in front of it and a rock is on the floor nearby.")
    guard = Npc("guard", "He's standing in front of the town gate. Looks angry...")
    rock = Item("rock", "A small rock. No bigger than your palm.")
    main_street = Location("Main street", "The main street of town")
    shield = Armour("shield", "a solid shield to protect you!", 50, 25)
    sword = Weapon("sword", "ouch it's sharp!", 100, 20)
    man = Npc("man", "he's carrying a cool walking stick")
    front_gate.add_item(sword)
    front_gate.add_item(rock)
    front_gate.add_item(shield)
    front_gate.add_path({"north": main_street})
    parser = Parser(player, front_gate)

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

        use_sentence = "use sword"
        parsed_use = self.parser.parse(use_sentence)
        self.assertTrue(isinstance(parsed_use, Use))
        self.assertEqual(parsed_use.subj, self.player)
        self.assertEqual(parsed_use.obj, self.sword)

    def test_parse_move(self):

        move_sentence = "travel north"
        parsed_move = self.parser.parse(move_sentence)
        self.assertTrue(isinstance(parsed_move, Move))
        self.assertEqual(parsed_move.subj, self.player)
        self.assertEqual(parsed_move.obj, self.main_street)





