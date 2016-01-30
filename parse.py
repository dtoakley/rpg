from verb import *


class Parser(object):

    def __init__(self, player, location):
        self.player = player
        self.location = location
        self.pickup = ["take", "pickup", "get", "grab"]
        self.lookat = ["lookat", "show", "see", "check"]
        self.use = ["use", "wield", "hold", "throw", "give"]
        self.move = ["go", "move", "walk", "travel"]

    def parse(self, sentence):
        # takes a sentence and returns a verb instance applied to the sentence object

        words = sentence.split()
        words[1].capitalize()

        if words[0] in self.pickup:
            try:
                obj = self.location.search_objects(words[1])
                return PickUp(self.player, obj)
            except AttributeError:
                print "object not found!"

        if words[0] in self.lookat:
            if words[1] == "inventory":
                inventory = self.player.get_inventory()
                print inventory

            else:
                try:
                    obj = self.location.search_objects(words[1])
                    return LookAt(self.player, obj)
                except AttributeError:
                    print "object not found!"

        if words[0] in self.use:
            try:
                obj = self.location.search_objects(words[1])
                return Use(self.player, obj)
            except AttributeError:
                print "object not found!"

        if words[0] in self.move:
            try:
                obj = self.location.paths.get(words[1])
                return Move(self.player, obj)
            except AttributeError:
                print "object not found!"










