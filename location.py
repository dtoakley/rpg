class Location(object):

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []
        self.characters = []
        self.paths = {}
        self.first_time = True

    def add_item(self, item):
        self.items.append(item)
        return item

    def add_character(self, character):
        self.characters.append(character)
        return character

    def add_path(self, path):
        self.paths.update(path)
        return path













