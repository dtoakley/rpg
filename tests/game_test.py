import unittest

from character import *
from item import *
from location import *
from lexicon import *
from game import *
from itertools import chain


class TestGame(unittest.TestCase):
    game = Game("Winterforge")
    game.build('test_game_data.json')

    def tests_get_and_parse_game_data(self):
        items, characters, locations = self.game.get_and_parse_game_data('test_game_data.json')

        self.assertTrue(len(items), 10)
        self.assertTrue(type(characters), dict)
        self.assertIn("tavern", locations)
        self.assertIn("paths", locations["general_store"])
        self.assertNotIn("wonderland", locations)

    def test_add_locations(self):
        locations = self.game.locations
        location_names = []

        self.assertEqual(len(locations), 4)

        for location in locations:
            self.assertIsInstance(location, Location)
            location_names.append(location.name)

        self.assertEqual(location_names, ['Tavern', 'Front gate', 'Main street', 'General store'])

    def test_add_characters(self):
        pass

    def test_add_items(self):
        pass

    def test_parse_underscore_string(self):
        string = "name_with_underscores"
        self.assertEqual("Name with underscores", self.game.parse_underscore_string(string))

    def test_play(self):
        pass
        #self.game.play()
