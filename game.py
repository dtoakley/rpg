from character import *
from lexicon import *
from location import *
from item import *


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

    def build_lexicon(self, game_data):
        lexicon = Lexicon()
        lexicon.build_lexicon(game_data)

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


paths = ["north", "south", "east", "west"]
verbs = ["pick", "look", "move", "take"]
nouns = ["sword", "old man", "gate"]
ignores = ["the", "in", "of", "a"]
front_gate = Location("Front Gate of Town", "You are at the front gate."
                                            " It is locked and there is an old man standing nearby.")
town_center = Location("The Town Center", "You're in the centre of town!")

front_gate.add_path({"north": town_center})
sword = Weapon("sword", "a sharp blade", 10, 20)
front_gate.add_item(sword)
old_man = Npc("old man", "maybe he know how to open the gate!")
front_gate.add_character(old_man)

town_center.add_path({"south": front_gate})

lexi = Lexicon(paths, verbs, nouns, ignores)

locations = {front_gate, town_center}

game = Game("a test game")

game.play(lexi, front_gate)



