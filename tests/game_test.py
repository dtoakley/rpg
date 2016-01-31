import unittest

from character import *
from item import *
from location import *
from game import *


class TestGame(unittest.TestCase):
    game = Game("Winterforge")
    game_data = game.get_and_parse_json_data('test_game_data.json', 'locations')
    game.build_game(game_data)

    def tests_get_and_parse_game_data(self):
        # gets data from json file and returns it as a dict.

        self.assertEqual(type(self.game_data), list)
        # TODO more parser tests

    def test_add_locations(self):
        # takes game data, build location objects and adds them to the game

        self.assertEqual(len(self.game.locations), 4)
        self.assertEqual(self.game.locations[0].name, "Front gate")
        self.assertTrue(self.game.locations[0].travelable)
        self.assertFalse(self.game.locations[1].travelable)

    def test_add_characters(self):
        # takes game data, builds character objects and adds them to locations
        self.assertEqual(self.game.locations[0].characters[0].name, "Guard")
        self.assertEqual(self.game.locations[1].characters[1].name, "Young boy")
        self.assertEqual(self.game.locations[3].characters[0].name, "General store manager")

    def test_add_items(self):

        self.assertEqual(self.game.locations[0].characters[0].items[0].name, "Town key")
        self.assertEqual(self.game.locations[1].characters[1].items[0].name, "Yo yo")
        self.assertEqual(self.game.locations[2].characters[0].items[0].name, "Tavern key")
        self.assertEqual(self.game.locations[3].items[0].name, "Wanted poster")

    def test_parse_underscore_string(self):
        string = "name_with_underscores"
        self.assertEqual("Name with underscores", self.game.parse_underscore_string(string))

    def test_add_paths(self):

        print self.game.locations[0].paths.get('north').name
        self.assertEqual(self.game.locations[0].paths.get('north').name, "Main street")
        self.assertEqual(self.game.locations[1].paths.get('west').name, "General store")
        self.assertEqual(self.game.locations[2].paths.get('west').name, "Main street")
        self.assertEqual(self.game.locations[3].paths.get('east').name, "Main street")

    def test_add_events(self):

        self.assertTrue(self.game.locations[0].event)
        self.assertEqual(self.game.locations[0].event.get("action_object"), "rock")
        self.assertEqual(self.game.locations[0].event.get("action_verb"), "use")
        self.assertEqual(self.game.locations[0].event.get("reaction_verb"), "can_travel")
        self.assertEqual(self.game.locations[0].event.get("reaction_object"), "Main street")
        self.assertEqual(self.game.locations[0].event.get("reaction_desc"), "You threw the rock at the guard. it knocked him over in one!")

    def test_play(self):
        self.game.play()
        pass
