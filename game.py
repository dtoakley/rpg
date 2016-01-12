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

    @staticmethod
    def get_player_input(prompt=">> "):
        input = raw_input(prompt + " ")
        return input

    @staticmethod
    def parse_underscore_string(name):
        return name.capitalize().replace("_", " ")

    def get_and_parse_json_data(self, data, data_type):
        with open(data) as data_file:
            json_game_data = self.byteify(json.load(data_file))
            return json_game_data[data_type]

    def build_game(self, game_data):

        for location, data in enumerate(game_data):
            loc_characters = data.get('characters')
            loc_items = data.get('items')
            loc_obj = self.build_object(data, Location, 'paths')

            for character in loc_characters:
                char_obj = self.build_object(character, Character)
                loc_obj.add_character(char_obj)
                char_items = character.get('items')

                for char_item in char_items:
                    char_item_obj = self.build_object(char_item, Item, 'value')
                    char_obj.add_item(char_item_obj)

            for loc_item in loc_items:
                loc_item_obj = self.build_object(loc_item, Item)
                loc_obj.add_item(loc_item_obj)

            self.locations.append(loc_obj)

    def build_object(self, data, cls, attr=None):
        obj_name = self.parse_underscore_string(data.get('name'))
        obj_desc = data.get('desc')
        if attr:
            obj_attr = data.get(str(attr))
            new_obj = cls(obj_name, obj_desc, obj_attr)
        else:
            new_obj = cls(obj_name, obj_desc)

        return new_obj

    def byteify(self, data_input):
        if isinstance(data_input, dict):
            return {self.byteify(key): self.byteify(value) for key, value in data_input.iteritems()}
        elif isinstance(data_input, list):
            return [self.byteify(element) for element in data_input]
        elif isinstance(data_input, unicode):
            return data_input.encode('utf-8')
        else:
            return data_input

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
                action_desc = lexicon.get_action_from_sentence(self.get_player_input())
                action_to_do = player.process_action(action_desc)
                player.do_action(action_to_do)



