class Game(object):

    def __init__(self, name):
        self.name = name
        self.player = None
        self.locations = []

    def set_name(self, name):
        self.name = name
        return name

    def add_location(self, location):
        self.locations.append(location)
        return location

