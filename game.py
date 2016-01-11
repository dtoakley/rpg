from character import *
from lexicon import *
from location import *
from item import *
import json
from pprint import pprint


class Game(object):

    def __init__(self, name):
        self.name = name
        self.player = Player()
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)
        return location

    @staticmethod
    def get_player_input(prompt=">> "):
        input = raw_input(prompt + " ")
        return input

    def build(self, game_data):
        item_data, character_data, locations_data = self.get_and_parse_game_data(game_data)
        try:
            self.add_locations(item_data, locations_data, character_data)
        except Exception as e:
            print "Error building game:" + e.message

    def get_and_parse_game_data(self, game_data):
        # parses JSON game data and returns locations, characters and items.
        # May want to return that data as a dict so that order doesn't make. More composable that way.
        with open(game_data) as data_file:
            json_game_data = self.byteify(json.load(data_file))
            return json_game_data.get("items"), json_game_data.get("characters"), json_game_data.get("locations")

    def add_locations(self, item_data, locations_data, character_data):
        # Need to refactor and abstract this and the other object adders. They shouldn't be aware of each other.
        for location, data in locations_data.iteritems():
            name = self.parse_underscore_string(location)
            desc = data.get('desc')
            loc_item_list = data.get('items')
            loc_char_list = data.get('characters')
            paths = data.get('paths')

            loc_obj = Location(name, desc, paths)

            self.add_items(item_data, loc_item_list, loc_obj)
            self.add_characters(character_data, loc_char_list, item_data, loc_obj)
            self.locations.append(loc_obj)

    def add_characters(self, character_data, loc_char_list, item_data, loc_obj):

        for character, data in character_data.iteritems():
            char_name = self.parse_underscore_string(character)
            desc = data.get('desc')
            char_item_list = data.get('items')

            # create character instances and add items to them
            char_obj = Character(char_name, desc)
            if char_name in loc_char_list:
                loc_obj.characters.append(char_obj)
            self.add_items(item_data, char_item_list, char_obj)

    def add_items(self, item_data, char_or_loc_lists, char_or_loc_obj):
        for item, attr in item_data.iteritems():
            item_name = self.parse_underscore_string(item)
            if item_name in char_or_loc_lists:
                item_obj = Item(item_name, attr["desc"], attr["value"])
                char_or_loc_obj.items.append(item_obj)

    def byteify(self, data_input):
        if isinstance(data_input, dict):
            return {self.byteify(key):self.byteify(value) for key, value in data_input.iteritems()}
        elif isinstance(data_input, list):
            return [self.byteify(element) for element in data_input]
        elif isinstance(data_input, unicode):
            return data_input.encode('utf-8')
        else:
            return data_input

    @staticmethod
    def parse_underscore_string(name):
        return name.capitalize().replace("_", " ")


    # game loop
    def play(self, lexicon, first_location):
        player = Player()
        player.set_player_name(self.get_player_input("What is your name, young adventurer?"), self.name)
        player.set_location(first_location)

        first_location.add_character(player)

        while player.is_alive and not player.is_victorious:
            location = player.current_location
            location.load()

            if player.is_alive and not player.is_victorious:
                action = lexicon.convert_sentence_to_action(self.get_player_input())
                print action



