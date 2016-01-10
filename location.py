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

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
            else:
                pass

    def get_character(self, character_name):
        for character in self.characters:
            if character.name == character_name:
                return character
            else:
                pass

    def search_objects(self, name):
        for obj in [self.characters, self.items, self.paths]:
            if name in obj:
                return obj
            else:
                pass

    def get_desc(self):
        return self.desc

    def load(self):
        print self.desc

        if self.first_time:
            self.first_time_event()
            self.first_time = False

    def first_time_event(self):
        print "first time event!"




